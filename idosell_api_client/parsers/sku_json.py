import json
from .base_json import BaseJSONParser


class SKUJSONParser(BaseJSONParser):
    def parse(self):
        product_id = self.get_product_id()
        data = {
            "product_id": product_id,
        }

        return json.dumps(data, indent=4)

    def get_product_id(self):
        if self.has_error:
            return self.error_message  # Return the error message or simply return None
        return {"id": self.data["results"][0]["productSkuList"][0].get("productId")}

    def get_data(self):
        # Implement SKU-specific data retrieval logic
        pass
