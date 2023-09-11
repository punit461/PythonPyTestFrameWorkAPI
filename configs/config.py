import configparser
import os
from tests import project_directory
import tests.base as base


# Initialize the configparser
class ConfigReader:
    """
        A class for reading configuration from an INI file.
    """

    def __init__(self, config_path=None):
        """
           Initialize the ConfigReader.
           Args: config_path (str): The path to the configuration INI file.
        """
        if config_path is None:
            config_path = os.path.join(project_directory, 'configs', 'config.ini')
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

    def get_value(self, section, key):
        return self.config.get(section, key)

    def set_value(self, section, key, value):
        if section not in self.config:
            self.config.add_section(section)
        self.config.set(section, key, value)

    def save_config(self):
        with open(self.config_path, 'w') as config_file:
            self.config.write(config_file)

    # Read data from the 'URLs' section
    def get_protocol(self):
        return self.get_value('URLs', 'protocol')

    def get_domain(self):
        return self.get_value('URLs', 'domain')

    def get_subdomain(self):
        base_env = self.get_value('URLs', 'baseEnv')
        if base_env == "testEnv":
            return self.get_value('URLs', 'testEnv')
        elif base_env == "devEnv":
            return self.get_value('URLs', 'devEnv')
        elif base_env == "stageEnv":
            return self.get_value('URLs', 'stageEnv')
        elif base_env == "prodEnv":
            return self.get_value('URLs', 'prodEnv')
        else:
            base.temp_company()
            return self.get_value('URLs', 'tempEnv')

    # Read data from the 'Credentials' section
    def get_username(self):
        base_env = self.get_value('URLs', 'baseEnv')
        if base_env == "tempEnv":
            return self.get_value('Credentials', 'temp_username')
        else:
            return self.get_value('Credentials', 'username_admin')

    def get_password(self):
        base_env = self.get_value('URLs', 'baseEnv')
        if base_env == "tempEnv":
            return self.get_value('Credentials', 'temp_password')
        else:
            return self.get_value('Credentials', 'password_admin')

    # Read data from the 'Paths' section
    def get_api(self):
        return self.get_value('Paths', 'api')

    def get_login(self):
        return self.get_value('Paths', 'login')

    def get_cost_center(self):
        return self.get_value('Paths', 'cost_center')

    def get_register(self):
        return self.get_value('Paths', 'register')

    def get_set_password(self):
        return self.get_value('Paths', 'setpassword')

    def get_log_mode(self):
        return self.get_value('Automation', 'log_mode')
