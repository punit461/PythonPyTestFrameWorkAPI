import requests
from utils.common import random_string

# base url definition
base_url = "https://mailsac.com/api"
temp_domain = "@mailsac.com"
# Define mail_sac Mail API endpoints
address_path = "/addresses"
validations_path = "/validations"
messages_path = "/messages"
text_path = "/text"

# headers
# get the mail-sac key from mailsac.com register and get the token for yourself.
headers = {'Mailsac-Key': 'k_8FFrtLBacU3IhyKmPRd7gbLPsG9OkdjWbIKvp3nUa368I79'}


# method to create a random email
def random_email():
    return random_string(10) + temp_domain


# method to generate temp email and validate the same.
def generate_temp_email(random_email_created):
    url = base_url + address_path + "/" + random_email_created
    response = requests.get(url=url, headers=headers)
    print(url, response)

    # validate response of request
    assert response.status_code == 200

    # validate the email created is disposable
    url2 = base_url + validations_path + address_path + "/" + random_email_created
    response2 = requests.get(url=url2, headers=headers)
    print(url2, response2)

    # validate response whether is disposable
    json_data = response2.json()
    disposable_email = str(json_data["isDisposable"])
    assert disposable_email.lower().__contains__("true")


# method to read the email
def read_email(temp_email):
    url = base_url + address_path + "/" + temp_email + messages_path
    response = requests.get(url=url, headers=headers)
    print(url, response)
    print(response.json())

    json_data = response.json()
    try:
        # store message id
        msg_id = json_data[0]["_id"]
        assert response.status_code == 200

        # read email body
        url2 = base_url + text_path + "/" + temp_email + "/" + msg_id
        response2 = requests.get(url=url2, headers=headers)
        assert response.status_code == 200
        print(response2.text)

        return response2.text
    except ValueError:
        print("No mails in the Mail Box ")
        return None
