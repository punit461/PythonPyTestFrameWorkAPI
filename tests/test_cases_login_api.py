import os
import sys
import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.common import get_json
from utils.common import assert_status_code
from utils.common import assert_json_value
from tests.base import setup
from utils.custom_logger import logmethod
from apis.apis import APIClient


@pytest.mark.usefixtures("setup")
class TestLoginAPI:

    @logmethod
    def test_successful_login(self, setup):
        config_reader = setup
        api = APIClient(config_reader)

        json = {'email': config_reader.get_username(), 'password': config_reader.get_password()}

        resp = api.api_login(json)
        json_data = get_json(resp)
        print(json_data)
        assert_status_code(resp, 200)
        assert_json_value(json_data, 'status', "OK")

    @logmethod
    def test_successful_login2(self, setup):
        config_reader = setup
        api = APIClient(config_reader)

        json = {'email': config_reader.get_username(), 'password': config_reader.get_password()}

        resp = api.api_login(json)
        json_data = get_json(resp)
        print(json_data)
        assert_status_code(resp, 200)
        assert_json_value(json_data, 'status', "OK")
