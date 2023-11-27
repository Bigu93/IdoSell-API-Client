import requests
import requests.packages
import logging
from typing import List, Dict
from exceptions.api_exceptions import IdoSellApiException
from json import JSONDecodeError
from models.response import Response

DEFAULT_TIMEOUT = 10  # seconds


class BaseClient:
    def __init__(
        self,
        hostname: str,
        auth_token: str = "",
        version: str = "v1",
        ssl_verify: bool = True,
        logger: logging.Logger = None,
    ):
        """
        Constructor for BaseClient class
        :param hostname: website url
        :param auth_token: authentication token
        :param version: v1
        :param ssl_verify: Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger: (optional) If your app has a logger, pass it in here.
        """
        self._logger = logger if logger else logging.getLogger(__name__)
        self.url = f"{hostname}/{version}/"
        self.auth_token = auth_token
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def get(self, endpoint: str, ep_params: Dict = None) -> Response:
        return self._send_request(
            http_method="GET", endpoint=endpoint, ep_params=ep_params
        )

    def post(
        self, endpoint: str, ep_params: Dict = None, data: Dict = None
    ) -> Response:
        return self._send_request(
            http_method="POST", endpoint=endpoint, ep_params=ep_params, data=data
        )

    def delete(
        self, endpoint: str, ep_params: Dict = None, data: Dict = None
    ) -> Response:
        return self._send_request(
            http_method="DELETE", endpoint=endpoint, ep_params=ep_params, data=data
        )

    def _send_request(
        self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None
    ) -> Response:
        full_url = self.url + endpoint
        headers = {"Authorization": f"Bearer {self.auth_token}"}

        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ", ".join(
            (log_line_pre, "success={}, status_code={}, message={}")
        )

        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(
                method=http_method,
                url=full_url,
                verify=self._ssl_verify,
                headers=headers,
                timeout=DEFAULT_TIMEOUT,
                params=ep_params,
                json=data,
            )
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise IdoSellApiException("Request failed") from e

        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise IdoSellApiException("Bad JSON in response") from e

        is_success = response.status_code == 200
        log_line = log_line_post.format(
            is_success, response.status_code, response.reason
        )

        if is_success:
            self._logger.debug(msg=log_line)
            return Response(
                response.status_code, message=response.reason, data=data_out
            )
        self._logger.error(msg=log_line)
        raise IdoSellApiException(f"{response.status_code}: {response.reason}")
