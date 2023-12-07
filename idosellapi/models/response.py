from idosellapi.models.product import Product, Authenticate, Errors, Result


class Response:
    def __init__(self, status_code: int, message: str = "", data: list[dict] = None):
        """
        Result returned from low-level BaseClient class
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []
