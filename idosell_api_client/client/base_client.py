import requests
from auth import Auth

# import exceptions


class BaseClient:
    def __init__(self, base_url, auth_instance):
        self.base_url = base_url
        self.auth_instance = auth_instance
        self.headers = {}

    def _update_headers(self):
        self.headers["Authorization"] = f"Bearer {self.auth_instance.get_token()}"

    def get(self, endpoint, params=None):
        self._update_headers()
        return self._send_request("GET", endpoint, params=params)

    def post(self, endpoint, data=None):
        self._update_headers()
        return self._send_request("POST", endpoint, json=data)

    def put(self, endpoint, data=None):
        self._update_headers()
        return self._send_request("PUT", endpoint, json=data)

    def delete(self, endpoint):
        self._update_headers()
        return self._send_request("DELETE", endpoint)

    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise APIError(f"API Error: {e.response.status_code} - {e.response.text}")


auth_instance = Auth(client_username, client_secret, base_url)
client = BaseClient(base_url, auth_instance)
