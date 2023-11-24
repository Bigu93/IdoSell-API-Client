import json


def error_check(func):
    def wrapper(self, *args, **kwargs):
        if self.has_error:
            return self.error_message
        return func(self, *args, **kwargs)

    return wrapper


class BaseJSON:
    def __init__(self, json_data, result_key="results"):
        self.data = json_data
        self.result_key = result_key
        self.has_error = False
        self.error_message = self.check_for_errors()

    def show(self, *keys):
        if not hasattr(self, "parsed_data"):
            raise ValueError("Data has not been parsed yet.")

        if keys:
            selected_data = {key: self.parsed_data.get(key) for key in keys}
        else:
            selected_data = self.parsed_data

        return json.dumps(selected_data, indent=4, ensure_ascii=False)

    def to_dict(self, *keys):
        if not hasattr(self, "parsed_data"):
            raise ValueError("Data has not been parsed yet.")

        if keys:
            selected_data = {key: self.parsed_data.get(key) for key in keys}
        else:
            selected_data = self.parsed_data

        return selected_data

    def check_for_errors(self):
        error_info = self.data.get("errors", {})
        fault_code = error_info.get("faultCode", 0)
        fault_string = error_info.get("faultString", "")

        if fault_code != 0 or fault_string:
            self.has_error = True
            return {"error": True, "message": fault_string, "code": fault_code}

        if not self.data.get(self.result_key):
            self.has_error = True
            return {
                "error": True,
                "message": f"{self.result_key.capitalize()} not found",
                "code": -1,
            }

        return {"error": False}

    def parse(self):
        raise NotImplementedError("This method should be implemented in a subclass")
