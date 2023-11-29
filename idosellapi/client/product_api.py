import logging
from .base_client import BaseClient
from exceptions.api_exceptions import IdoSellApiException
from models.response import Response


class ProductApi:
    def __init__(
        self,
        hostname: str,
        auth_token: str,
        ver: str = "v1",
        ssl_verify: bool = True,
        logger: logging.Logger = None,
    ):
        self._base_client = BaseClient(hostname, auth_token, ver, ssl_verify, logger)

    def get_products(self, params) -> Response:
        result = self._base_client.post(endpoint="products/products/get", data=params)
        return result
