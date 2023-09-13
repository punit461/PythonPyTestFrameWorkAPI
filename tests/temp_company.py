import os
import re
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils.mail_grabber as temp_mail
import utils.common as commons


def temp_company():
    from configs.config import ConfigReader
    config_reader = ConfigReader()

    # headers
    headers = {"Content-Type": "application/json",
               "Accept": "*/*",
               "Accept-Encoding": "gzip, deflate, br",
               "Connection": "keep-alive"}

    # url & paths
    subdomain2 = config_reader.get_subdomain2()
    if subdomain2 == "":
        base_url = str(config_reader.get_protocol() + config_reader.get_domain())
    else:
        base_url = str(config_reader.get_protocol() + subdomain2 + "." + config_reader.get_domain())
    path = config_reader.get_api() + config_reader.get_register()

    # Pre-setup
    email = temp_mail.random_email()  # create a random mail
    temp_mail.generate_temp_email(email)  # random email + mailbox created
    config_reader.set_value(section="Credentials",
                            key="temp_username",
                            value=email)
    config_reader.save_config()  # save the random email generated for further use.

    # Json Body of Register API Request
    json = {'email': str(email),
            "fullName": commons.random_string(8),
            "companyName": commons.random_string(10),
            "domainName": commons.random_string(10),
            "phone": commons.random_num(10)
            }

    # create a new company and send the verification link in mail
    resp = commons.send_request('POST', url=base_url + path, headers=headers, json_body=json)
    commons.assert_status_code(resp, 201)

    # read the mailbox to get the link from mail
    time.sleep(10)
    text = temp_mail.read_email(email)

    if text is None:
        raise ValueError("No Mails in the Mailbox")
    else:
        # Define a regular expression pattern to match the URL
        url_pattern = r'(https?)://([a-z0-9]+)\.?(.+)?\.devassisto\.com/verify\?token=([\w-]+)'

        # Use the re.search function to find the URL in the text
        match = re.search(url_pattern, text)

        if match:
            # Extract the subdomain and token
            subdomain = match.group(2)
            token = match.group(4)

            print("Subdomain:", subdomain)
            print("Token:", token)
            config_reader.set_value(section="URLs",
                                    key="temp_env",
                                    value=subdomain)
            config_reader.set_value(section="URLs",
                                    key="token",
                                    value=token)
            config_reader.save_config()

            # Set Password API

            # url & paths
            if subdomain2 == "":
                base_url = str(config_reader.get_protocol() + subdomain + "." + config_reader.get_domain())
            else:
                base_url = str(
                    config_reader.get_protocol() + subdomain + "." + subdomain2 + "." + config_reader.get_domain())

            path = config_reader.get_api() + config_reader.get_set_password()

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
                                        url=base_url + path,
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
