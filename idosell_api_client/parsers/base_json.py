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

    @error_check
    def show(self, *keys, product_index=None):
        selected_data = self._select_nested_data(*keys, product_index=product_index)
        return json.dumps(selected_data, indent=4, ensure_ascii=False)

    @error_check
    def to_dict(self, *keys, product_index=None):
        return self._select_nested_data(*keys, product_index=product_index)

    def _select_nested_data(self, *keys, product_index=None):
        if not hasattr(self, "parsed_data"):
            raise ValueError("Data has not been parsed yet.")

        if "products" in self.parsed_data:
            if product_index is not None:
                # Extract data for a specific product
                return self._extract_data_from_product(
                    self.parsed_data["products"], keys, product_index
                )

            # Extract data for all products
            return [
                self._extract_data_from_product(
                    self.parsed_data["products"], keys, index
                )
                for index in range(len(self.parsed_data["products"]))
            ]

        return self._extract_data(self.parsed_data, keys)

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

    def get_path(self):
        raise NotImplementedError("This method should be implemented in a subclass")

    @staticmethod
    def _extract_data_from_product(products, keys, index):
        if index >= len(products):
            raise IndexError("Product index out of range.")

        product_data = products[index]
        return BaseJSON._extract_data(product_data, keys)

    @staticmethod
    def _extract_data(data, keys):
        if not keys:
            return data

        return {key: data.get(key) for key in keys if key in data}
