from typing import List, Dict
from .product import Product, Authenticate, Errors, Result


class Response:
    def __init__(self, status_code: int, message: str = "", data: List[Dict] = None):
        """
        Result returned from low-level BaseClient class
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []


def process_response(response_data: Dict) -> Product:
    """
    Process the response from the API and return a Product object
    :param response_data: Python Dictionary of the response from the API
    :return: Product object
    """
    authenticate = Authenticate(**response_data["authenticate"])
    errors = Errors(**response_data["errors"])
    results = [Result(**product_data) for product_data in response_data["results"]]

    product = Product(
        authenticate=authenticate,
        resultsPage=response_data["resultsPage"],
        resultsLimit=response_data["resultsLimit"],
        resultsNumberPage=response_data["resultsNumberPage"],
        resultsNumberAll=response_data["resultsNumberAll"],
        errors=errors,
        results=results,
    )

    return product
