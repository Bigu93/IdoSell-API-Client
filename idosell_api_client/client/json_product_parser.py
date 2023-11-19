import json
from exceptions.api_exceptions import APIError


class JSONParser:
    def __init__(self, json_data):
        self.data = json_data
        self.check_for_errors()

    def check_for_errors(self):
        error_info = self.data.get("errors", {})
        fault_code = error_info.get("faultCode")
        fault_string = error_info.get("faultString")

        if fault_code != 0 or fault_string:
            raise APIError(fault_string, fault_code)


