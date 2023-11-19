import json
from exceptions.api_exceptions import APIError


class BaseJSONParser:
    def __init__(self, json_data):
        self.data = json_data
        self.has_error = False  # Instance variable to track if an error occurred
        self.error_message = self.check_for_errors()

    def check_for_errors(self):
        error_info = self.data.get("errors", {})
        fault_code = error_info.get("faultCode")
        fault_string = error_info.get("faultString")

        if fault_code != 0 or fault_string:
            self.has_error = True
            return {"error": True, "message": fault_string, "code": fault_code}

        if not self.data.get("results"):
            self.has_error = True
            return {"error": True, "message": "No results found", "code": -1}

        return {"error": False}

    def _get_product_id(self):
        if self.has_error:
            return self.error_message

        return self.data["results"][0].get("productId")

    def parse(self):
        raise NotImplementedError("This method should be implemented in a subclass")
