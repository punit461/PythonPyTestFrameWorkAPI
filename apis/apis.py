from configs.config import ConfigReader
from utils.common import send_request


class APIClient:
    headers = {"Content-Type": "application/json",
               "Accept": "*/*",
               "Accept-Encoding": "gzip, deflate, br",
               "Connection": "keep-alive"}

    def __init__(self, config_reader):
        # Initialise classes
        self.base_url = None
        self.config_reader = config_reader

        # Set the URL
        http = self.config_reader.get_protocol()
        subdomain = self.config_reader.get_subdomain()
        subdomain2 = self.config_reader.get_subdomain2()
        domain = self.config_reader.get_domain()
        if subdomain2 == "":
            print("domain2 is blank")
            self.sub_url = str(http + domain)
            self.base_url = str(http + subdomain + "." + domain)
        else:
            print("domain2 is  not ...blank")
            self.sub_url = str(http + subdomain2 + "." + domain)
            self.base_url = str(http + subdomain + "." + subdomain2 + "." + domain)

    def api_register(self, json):
        # get the path of api and use to concatenate with url
        path = self.config_reader.get_api() + self.config_reader.get_register()

        # Send the request
        response = send_request('POST',
                                url=self.sub_url + path,
                                headers=APIClient.headers,
                                json_body=json)
        return response

    def api_set_password(self, token, json):
        # get the path of api and use to concatenate with url
        path = self.config_reader.get_api() + self.config_reader.get_set_password()

        # add parameters
        params = {'token': token}

        # Send the request
        response = send_request('POST',
                                url=self.base_url + path,
                                headers=APIClient.headers,
                                params=params,
                                json_body=json)
        return response

    def api_login(self, json):
        # get the path of api and use to concatenate with url
        path = self.config_reader.get_api() + self.config_reader.get_login()

        # Send the request
        response = send_request('POST',
                                url=self.base_url + path,
                                headers=APIClient.headers,
                                json_body=json)
        return response
