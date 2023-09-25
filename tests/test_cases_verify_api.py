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
class TestVerifyAPI:

    @allure.story("Verify API TC - Valid Email ")
    @allure.title("verify Verify api with valid Email")
    @logmethod
    def test_valid_verify_email(self, setup):
        logger = setup_custom_logger(self.test_valid_verify_email.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        params = {'email': config_reader.get_username()}

        resp = api.api_verify(params)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 200)
        assert_json_value(json_data, 'status', "OK")

    @allure.story("Verify API TC - Valid token ")
    @allure.title("verify Verify api with valid token")
    @logmethod
    def test_valid_verify_token(self, setup):
        logger = setup_custom_logger(self.test_valid_verify_token.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        params = {'token': config_reader.get_token()}

        resp = api.api_verify(params)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 410)
        assert_json_value(json_data, 'status', "GONE")

    @allure.story("Verify API TC - Valid jwt_token ")
    @allure.title("verify Verify api with valid jwt_token")
    @logmethod
    def test_valid_verify_jwt_token(self, setup):
        logger = setup_custom_logger(self.test_valid_verify_jwt_token.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        params = {'jwt': config_reader.get_jwt_token()}

        resp = api.api_verify(params)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 200)
        assert_json_value(json_data, 'authority', "Super Admin")

    @allure.story("Verify API TC - Valid domain ")
    @allure.title("verify Verify api with valid domain")
    @logmethod
    def test_valid_verify_domain(self, setup):
        logger = setup_custom_logger(self.test_valid_verify_domain.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        params = {'domain': config_reader.get_subdomain()}

        resp = api.api_verify(params)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 200)
        assert_json_value(json_data, 'status', "OK")

    @allure.story("Verify API TC - Invalid Credentials ")
    @allure.title("verify Verify api with Invalid credentials")
    @logmethod
    def test_invalid_verify(self, setup):
        logger = setup_custom_logger(self.test_invalid_verify.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        params = {'email': "invalidemail@invalid.com"}

        resp = api.api_verify(params)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 404)
        assert_json_value(json_data, 'status', "NOT_FOUND")

    @allure.story("Verify API TC - Invalid Random Characters")
    @allure.title("verify Verify api with Invalid Random Characters")
    @logmethod
    def test_random_verify(self, setup):
        logger = setup_custom_logger(self.test_random_verify.__name__)
        config_reader = setup
        api = APIClient(config_reader)

        params = {'email': "(){}[]|`¬¦! £$%^&*<>:;#~_-+=,@@invalid.com"}

        resp = api.api_verify(params)
        json_data = get_json(resp)
        print(json_data)
        logger.info(f"Response & Request: {get_full_response(resp)}")
        assert_status_code(resp, 400)
        assert_json_value(json_data, 'status', "BAD_REQUEST")
