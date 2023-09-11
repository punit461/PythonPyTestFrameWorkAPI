import os
import re
import sys
import time

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from configs.config import ConfigReader
import utils.mail_grabber as temp_mail
import utils.common as commons


@pytest.fixture(scope="function", autouse=True)
def setup(request):
    config_reader = ConfigReader()
    http = config_reader.get_protocol()
    domain = config_reader.get_domain()
    subdomain = config_reader.get_subdomain()
    base_url = str(http + subdomain + "." + domain)

    request.cls.base_url = base_url
    request.cls.config_reader = config_reader

    yield base_url, config_reader

    # Add teardown code here
    current_test_name = request.node.name
    print(f"Test Case {current_test_name} Executed")


@pytest.fixture(scope="function", autouse=True)
def reg_setup(request):
    config_reader = ConfigReader()
    http = config_reader.get_protocol()
    domain = config_reader.get_domain()
    base_url = str(http + domain)

    request.cls.base_url = base_url
    request.cls.config_reader = config_reader

    yield base_url, config_reader

    # Add teardown code here
    current_test_name = request.node.name
    print(f"Test Case {current_test_name} Executed")


def temp_company():
    config_reader = ConfigReader()
    http = config_reader.get_protocol()
    domain = config_reader.get_domain()

    # url & paths
    base_url = str(http + domain)
    api = config_reader.get_api()
    register = config_reader.get_register()

    # headers
    headers = {"Content-Type": "application/json",
               "Accept": "*/*",
               "Accept-Encoding": "gzip, deflate, br",
               "Connection": "keep-alive"}

    # json body
    email = temp_mail.random_email()
    # saving the email in config file
    config_reader.set_value(section="Credentials",
                            key="temp_username",
                            value=email)
    config_reader.save_config()

    json = {'email': str(email),
            "fullName": commons.random_string(8),
            "companyName": commons.random_string(10),
            "domainName": commons.random_string(10),
            "phone": commons.random_num(10)
            }

    # perform operations
    temp_mail.generate_temp_email(email)  # random email + mailbox created

    # create a new company and send the verification link in mail
    resp = commons.send_request('POST', url=base_url + api + register, headers=headers, json_body=json)

    commons.assert_status_code(resp, 201)

    # read the mailbox to get the link from mail
    time.sleep(10)
    text = temp_mail.read_email(email)

    if text is None:
        raise ValueError("No Mails in the Mailbox")
    else:
        # Define a regular expression pattern to match the URL
        url_pattern = r'http://([\w.-]+)\.devassisto\.com/verify\?token=([\w-]+)'

        # Use the re.search function to find the URL in the text
        match = re.search(url_pattern, text)

        if match:
            # Extract the subdomain and token
            subdomain = match.group(1)
            token = match.group(2)

            print("Subdomain:", subdomain)
            print("Token:", token)
            config_reader.set_value(section="URLs",
                                    key="tempEnv",
                                    value=subdomain)
            config_reader.set_value(section="URLs",
                                    key="token",
                                    value=token)
            config_reader.save_config()

            # call the set password api and set password

            # url & paths
            base_url = str(http + subdomain + "." + domain)
            api = config_reader.get_api()
            set_password = config_reader.get_set_password()

            # headers
            headers = {"Content-Type": "application/json",
                       "Accept": "*/*",
                       "Accept-Encoding": "gzip, deflate, br",
                       "Connection": "keep-alive"}

            # params
            params = {"token": token}

            # json body
            password = commons.random_string(8)
            config_reader.set_value(section="Credentials",
                                    key="temp_password",
                                    value=password)
            json = {"newPassword": password}

            # set password for  new company
            resp = commons.send_request('POST',
                                        url=base_url + api + set_password,
                                        headers=headers,
                                        params=params,
                                        json_body=json)

            commons.assert_status_code(resp, 200)
            resp_json = commons.get_json(resp)
            jwt_token = resp_json["data"]["token"]

            config_reader.set_value(section="URLs",
                                    key="jwt_token",
                                    value=jwt_token)
            config_reader.save_config()

        else:
            print("URL not found in the text.")
