import requests
from exceptions.api_exceptions import APIError
from logs.logger import get_logger


class BaseClient:
    DEFAULT_TIMEOUT = 10  # seconds

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
            response = requests.request(
                method,
                url,
                headers=self.headers,
                timeout=self.DEFAULT_TIMEOUT,
                **kwargs,
            )
            response.raise_for_status()

            if "application/json" in response.headers.get("Content-Type", ""):
                self.logger.info(f"Response from {url}: {response.status_code}")
                return response.json()
            else:
                self.logger.info(f"Raw response from {url}: {response.text}")
                return response.text
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            if status_code == 404:
                error_message = "Resource not found"
            elif status_code == 401:
                error_message = "Unauthorized access"
            elif status_code == 500:
                error_message = "Internal server error"
            else:
                error_message = f"HTTP Error: {status_code}"
            self.logger.error(f"Error in {method} request to {url}: {error_message}")
            raise APIError(f"API Error: {status_code} - {error_message}")
        except requests.exceptions.Timeout as e:
            self.logger.error(f"Request to {url} timed out: {e}")
            raise APIError("Request timed out")
