import os
import sys
import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.common import get_json, get_full_response
from utils.common import assert_status_code
from utils.common import assert_json_value
from tests.base import setup
from utils.custom_logger import logmethod, setup_custom_logger
from apis.apis import APIClient


@pytest.mark.usefixtures("setup")
class TestLoginAPI:

    @allure.story("Login API TC - Valid Credentials ")
    @allure.title("Verify Login api with valid credentials")
    @logmethod
    def test_valid_login(self, setup):
        logger = setup_custom_logger(self.test_valid_login.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        json = {'email': config_reader.get_username(),
                'password': config_reader.get_password()
                }

        resp = api.api_login(json)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 200)
        assert_json_value(json_data, 'status', "OK")

    @allure.story("Login API TC - Invalid Credentials ")
    @allure.title("Verify Login api with invalid credentials")
    @logmethod
    def test_invalid_login(self, setup):
        logger = setup_custom_logger(self.test_invalid_login.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        json = {"email": "abcdxyzinvalid",
                "password": "abcdxyzinvalid"
                }

        resp = api.api_login(json)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 400)
        assert_json_value(json_data, 'status', "BAD_REQUEST")

    @allure.story("Login API TC - blank Credentials ")
    @allure.title("Verify Login api with blank credentials")
    @logmethod
    def test_blank_login(self, setup):
        logger = setup_custom_logger(self.test_blank_login.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        json = {"email": "",
                "password": ""
                }

        resp = api.api_login(json)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 400)
        assert_json_value(json_data, 'status', "BAD_REQUEST")

    @allure.story("Login API TC - blank body ")
    @allure.title("Verify Login api with blank body")
    @logmethod
    def test_blank_body_login(self, setup):
        logger = setup_custom_logger(self.test_blank_body_login.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        json = {}

        resp = api.api_login(json)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 400)
        assert_json_value(json_data, 'status', "BAD_REQUEST")
