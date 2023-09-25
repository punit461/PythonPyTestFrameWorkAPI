import os
import sys
import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.common import send_request, get_json, get_full_response
from utils.common import assert_status_code, assert_json_value
from utils.common import random_string, random_num
from tests.base import setup
from utils.custom_logger import logmethod, setup_custom_logger
from apis.apis import APIClient
import utils.mail_grabber as temp_mail


@pytest.mark.usefixtures("setup")
class TestRegisterAPI:

    @allure.story("Register API TC - Valid Details ")
    @allure.title("Verify Register API with Valid Details")
    @logmethod
    def test_valid_register(self, setup):
        logger = setup_custom_logger(self.test_valid_register.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        # create a temp email
        email = temp_mail.random_email()

        # create a temp mail-box
        temp_mail.generate_temp_email(email)

        # api body
        json = {'email': str(email),
                "fullName":     random_string(8),
                "companyName":  random_string(10),
                "domainName":   random_string(10),
                "phone":        random_num(10)
                }
        resp = api.api_register(json=json)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 201)
        assert_json_value(json_data, 'status', "CREATED")

    @allure.story("Register API TC - InValid Details ")
    @allure.title("Verify Register API with InValid Details")
    @logmethod
    def test_invalid_register(self, setup):
        logger = setup_custom_logger(self.test_valid_register.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        # api body
        json = {"email": "abcxyz.com",
                "fullName": random_string(8),
                "companyName": random_string(10),
                "domainName": "abcxyz@invalid.com",
                "phone": random_num(12)
                }
        resp = api.api_register(json=json)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 400)
        assert_json_value(json_data, 'status', "BAD_REQUEST")

