import configparser
import os
from tests import project_directory


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

    def get_base_env(self):
        return self.get_value('URLs', 'base_env')

    def get_subdomain(self):
        base_env = self.get_base_env()
        if base_env == "test_env":
            return self.get_value('URLs', 'test_env')
        elif base_env == "dev_env":
            return self.get_value('URLs', 'dev_env')
        else:
            return self.get_value('URLs', 'temp_env')

    def get_subdomain2(self):
        return self.get_value('URLs', 'subdomain2')

    def get_token(self):
        return self.get_value('URLs', 'token')

    def get_jwt_token(self):
        return self.get_value('URLs', 'jwt_token')

    # Read data from the 'Credentials' section
    def get_username(self):
        base_env = self.get_value('URLs', 'base_env')
        if base_env == "temp_env":
            return self.get_value('Credentials', 'temp_username')
        else:
            return self.get_value('Credentials', 'username_admin')

    def get_password(self):
        base_env = self.get_value('URLs', 'base_env')
        if base_env == "temp_env":
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

    def get_verify(self):
        return self.get_value('Paths', 'verify')

    def get_log_mode(self):
        return self.get_value('Automation', 'log_mode')
