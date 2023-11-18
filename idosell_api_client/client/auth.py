import requests
import time
import base64


class Auth:
    def __init__(self, client_username, client_secret, base_url):
        self.client_username = client_username
        self.client_secret = client_secret
        self.base_url = base_url
        self.access_token = None
        self.token_expires = 0

    def get_basic_auth_header(self):
        credentials = f"{self.client_username}:{self.client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded_credentials}"

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
