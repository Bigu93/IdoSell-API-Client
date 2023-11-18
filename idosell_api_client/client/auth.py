import requests
import time
import base64
import os
from dotenv import load_dotenv

load_dotenv()

client_username = os.getenv("IDOSELL_CLIENT_USERNAME")
client_secret = os.getenv("IDOSELL_CLIENT_SECRET")
base_url = os.getenv("IDOSELL_BASE_URL")


class Auth:
    def __init__(self, client_username, client_secret, base_url):
        self.client_username = client_username
        self.client_secret = client_secret
        self.base_url = base_url
        self.access_token = None
        self.token_expires = 0

    def is_token_valid(self):
        return self.access_token and time.time() < self.token_expires

    def get_token(self):
        if not self.is_token_valid():
            self.authenticate()
        return self.access_token

    def authenticate(self):
        try:
            url = f"{self.base_url}/api/authorize/1/authorize/accessToken"
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
            # Handle various types of HTTP errors and exceptions
            print(f"Error during authentication: {e}")
            self.access_token = None
            self.token_expires = 0
