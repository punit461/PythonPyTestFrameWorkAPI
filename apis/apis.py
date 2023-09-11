from configs.config import ConfigReader
from utils.common import send_request


class APIClient:

    def __init__(self):
        # Initialise classes
        self.config_reader = ConfigReader()

        # Set the URL
        http = self.config_reader.get_protocol()
        domain = self.config_reader.get_domain()
        subdomain = self.config_reader.get_subdomain()
        base_url = str(http + subdomain + "." + domain)
        self.base_url = base_url

    def api_login(self, json):
        # get the path of api and use to concatenate with url
        api = self.config_reader.get_api()
        login = self.config_reader.get_login()

        # headers
        headers = {"Content-Type": "application/json",
                   "Accept": "*/*",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Connection": "keep-alive"}

        # Send the request
        response = send_request('POST',
                                url=self.base_url + api + login,
                                headers=headers,
                                json_body=json)
        return response

    def api_set_password(self, token, json):
        # get the path of api and use to concatenate with url
        api = self.config_reader.get_api()
        set_password = self.config_reader.get_set_password()

        # headers
        headers = {"Content-Type": "application/json",
                   "Accept": "*/*",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Connection": "keep-alive"}

        # add parameters
        params = {'token': token}

        # Send the request
        response = send_request('POST',
                                url=self.base_url + api + set_password,
                                headers=headers,
                                params=params,
                                json_body=json)
        return response
