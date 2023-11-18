import requests
from exceptions.api_exceptions import APIError
from logs.logger import get_logger


class BaseClient:
    def __init__(self, base_url, auth_token):
        self.logger = get_logger(self.__class__.__name__)
        self.base_url = base_url
        self.auth_token = auth_token
        self.headers = {"Authorization": f"Bearer {self.auth_token}"}

    def get(self, endpoint, params=None):
        return self._send_request("GET", endpoint, params=params)

    def post(self, endpoint, data):
        return self._send_request("POST", endpoint, json=data)

    def put(self, endpoint, data):
        return self._send_request("PUT", endpoint, json=data)

    def delete(self, endpoint):
        return self._send_request("DELETE", endpoint)

    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        self.logger.info(f"Sending {method} request to {url}")
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            self.logger.info(f"Response from {url}: {response.status_code}")
            return response.json()
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"Error in {method} request to {url}: {e}")
            raise APIError(f"API Error: {e.response.status_code} - {e.response.text}")
