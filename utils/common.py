import string
import random
import requests
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from configs.config import ConfigReader


def random_string(length=10):
    random_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return random_str


def random_num(length=10):
    if length < 1:
        raise ValueError("Length must be at least 1")

    first_digit = str(random.randint(6, 9))
    rest_of_digits = [str(random.randint(0, 9)) for _ in range(length - 1)]
    return first_digit + ''.join(rest_of_digits)


def get_authorization_header():
    conf = ConfigReader()
    return {
        "Authorization": f"Bearer {conf.get_jwt_token}"
    }


def register_test_data(email):
    data = {
        "email": email,
        "fullName": random_string(),
        "companyName": random_string(),
        "domainName": random_string(),
        "phone": random_num()
    }
    return data


# Methods to Choose From   ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``
def send_request(method, url, auth=None, headers=None, params=None, data=None, json_body=None):
    response = requests.request(method=method,
                                url=url,
                                headers=headers,
                                params=params,
                                data=data,
                                auth=auth,
                                json=json_body,
                                verify=False)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    return response


def get_json(response):
    try:
        return response.json()
    except json.decoder.JSONDecodeError:
        print("Invalid JSON received in response")
        return None


def assert_status_code(response, expected_code):
    assert response.status_code == expected_code


def assert_json_value(resp_json, key, expected_value):
    assert resp_json.get(key) == expected_value


def assert_in_text(response, expected_msg):
    assert expected_msg in response
