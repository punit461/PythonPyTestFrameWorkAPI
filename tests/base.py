import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.custom_logger import setup_custom_logger
from configs.config import ConfigReader
import tests.temp_company as base


@pytest.fixture(scope="session", autouse=True)
def setup(request):
    config_reader = ConfigReader()

    # clear all temp values
    config_reader.set_value(section="URLs",
                            key="temp_env",
                            value="")
    # config_reader.set_value(section="URLs",
    #                         key="token",
    #                         value="")
    # config_reader.set_value(section="URLs",
    #                         key="jwt_token",
    #                         value="")
    config_reader.set_value(section="Credentials",
                            key="temp_username",
                            value="")
    config_reader.set_value(section="Credentials",
                            key="temp_password",
                            value="")
    config_reader.save_config()

    if ((config_reader.get_base_env() == "temp_env") and
            (config_reader.get_subdomain() == "")):
        base.temp_company()
        config_reader = ConfigReader()

    request.session.config_reader = config_reader

    yield config_reader

    # Add teardown code here
