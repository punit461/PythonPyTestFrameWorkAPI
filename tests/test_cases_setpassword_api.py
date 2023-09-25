import os
import sys
import time
import re

import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.common import get_json, get_full_response
from utils.common import assert_status_code
from utils.common import assert_json_value
from utils.common import random_string, random_num
from tests.base import setup
from utils.custom_logger import logmethod, setup_custom_logger
from apis.apis import APIClient
import utils.mail_grabber as temp_mail


@pytest.mark.usefixtures("setup")
class TestSetPasswordAPI:

    @allure.story("Set-Password API TC - Valid Details ")
    @allure.title("Verify Set-Password api with valid Details")
    @logmethod
    def test_valid_setpassword(self, setup):
        logger = setup_custom_logger(self.test_valid_setpassword.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        # Register api needs to be used before set-password can be used.

        # create a temp email
        email = temp_mail.random_email()

        # create a temp mail-box
        temp_mail.generate_temp_email(email)

        # api body
        reg_json = {'email': str(email),
                    "fullName": random_string(8),
                    "companyName": random_string(10),
                    "domainName": random_string(10),
                    "phone": random_num(10)
                    }
        reg_resp = api.api_register(json=reg_json)
        assert_status_code(reg_resp, 201)
        # reg_json_data = get_json(reg_resp)

        # wait for the mailbox to load all the emails
        time.sleep(10)

        # read the email
        text = temp_mail.read_email(email)

        if text is None:
            raise ValueError("No Mails in the Mailbox")
        else:
            # Define a regular expression pattern to match the URL
            url_pattern = r'(https?)://([a-z0-9]+)\.?(.+)?\.devassisto\.com/verify\?token=([\w-]+)'

            # Use the re.search function to find the URL in the text
            match = re.search(url_pattern, text)

            if match:
                # Extract token
                subdomain = match.group(2)
                token = match.group(4)
                print("Token:", token)
            else:
                raise ValueError("Invalid Mail in the Mailbox")

        json = {'newPassword': random_string(10)
                }

        resp = api.api_set_password(subdomain=subdomain,
                                    token=token, json=json)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 200)
        assert_json_value(json_data, 'status', "OK")

    @allure.story("Set-Password API TC - InValid Details ")
    @allure.title("Verify Set-Password api with Invalid password")
    @logmethod
    def test_invalid_setpassword(self, setup):
        logger = setup_custom_logger(self.test_invalid_setpassword.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        # Register api needs to be used before set-password can be used.

        # create a temp email
        email = temp_mail.random_email()

        # create a temp mail-box
        temp_mail.generate_temp_email(email)

        # api body
        reg_json = {'email': str(email),
                    "fullName": random_string(8),
                    "companyName": random_string(10),
                    "domainName": random_string(10),
                    "phone": random_num(10)
                    }
        reg_resp = api.api_register(json=reg_json)
        assert_status_code(reg_resp, 201)
        # reg_json_data = get_json(reg_resp)

        # wait for the mailbox to load all the emails
        time.sleep(10)

        # read the email
        text = temp_mail.read_email(email)

        if text is None:
            raise ValueError("No Mails in the Mailbox")
        else:
            # Define a regular expression pattern to match the URL
            url_pattern = r'(https?)://([a-z0-9]+)\.?(.+)?\.devassisto\.com/verify\?token=([\w-]+)'

            # Use the re.search function to find the URL in the text
            match = re.search(url_pattern, text)

            if match:
                # Extract token
                subdomain = match.group(2)
                token = match.group(4)
                print("Token:", token)
            else:
                raise ValueError("Invalid Mail in the Mailbox")

        json = {'newPassword': "(){}[]|`¬¦! £$%^&*<>:;#~_-+=,@"
                }

        resp = api.api_set_password(subdomain=subdomain,
                                    token=token, json=json)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 400)
        assert_json_value(json_data, 'status', "BAD_REQUEST")
