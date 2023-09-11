import os
import sys
import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.common import send_request
from utils.common import get_json
from utils.common import assert_status_code
from utils.common import assert_json_value
from tests.base import setup
from utils.custom_logger import logmethod


@pytest.mark.usefixtures("setup")
class TestLoginAPI:

    @logmethod
    def test_successful_login(self, setup):
        base_url, config_reader = setup
        api = config_reader.get_api()
        login = config_reader.get_login()

        json = {'email': config_reader.get_username(), 'password': config_reader.get_password()}

        resp = send_request('POST', url=base_url + api + login, json_body=json)
        json_data = get_json(resp)
        print(json_data)
        assert_status_code(resp, 200)
        assert_json_value(json_data, 'status', "OK")
