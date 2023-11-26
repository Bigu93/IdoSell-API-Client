import requests
import time
import base64
from logs.logger import get_logger
from exceptions.api_exceptions import IdoSellApiException


class Auth:
    BUFFER_TIME = 60  # seconds

    def __init__(self, client_username, client_secret, base_url):
        self.logger = get_logger(self.__class__.__name__)
        self.encoded_credentials = self.encode_credentials(
            client_username, client_secret
        )
        self.base_url = base_url
        self.access_token = None
        self.token_expires = 0

    @staticmethod
    def encode_credentials(client_username, client_secret):
        credentials = f"{client_username}:{client_secret}"
        return base64.b64encode(credentials.encode()).decode()

    def get_basic_auth_header(self):
        return f"Basic {self.encoded_credentials}"

    def is_token_valid(self):
        return self.access_token and time.time() < (
            self.token_expires - self.BUFFER_TIME
        )

    def get_token(self):
        if not self.is_token_valid():
            self.authenticate()
        return self.access_token

    def authenticate(self):
        try:
            url = f"https://butosklep.pl/api/authorize/1/authorize/accessToken"
            payload = {"grant_type": "client_credentials", "scope": ["api-pa"]}
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": self.get_basic_auth_header(),
            }

            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

            self.access_token = data["access_token"]
            self.token_expires = time.time() + int(data["expires_in"])

        except requests.RequestException as e:
            self.logger.error(f"Error in authentication request: {e}")
            raise IdoSellApiException(
                f"API Error: {e.response.status_code} - {e.response.text}"
            )
            self.access_token = None
            self.token_expires = 0
