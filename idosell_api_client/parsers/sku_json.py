import json
from .base_json import BaseJSON, error_check
from config.settings import STOCK_IDS


class SkuJSON(BaseJSON):
    def __init__(self, json_data):
        super().__init__(json_data)

    @error_check
    def parse(self):
        product_id = self._get_product_id()
        name = self._get_name().strip()
        size = self._get_size()
        code = self._get_producer_code()
        weight = self._get_weight()
        stock_quantities = self._get_stock_quantities()
        producer_name = self._get_producer_name()
        product_note = self._get_product_note()
        icons = self._get_product_icons()

        data = {
            "error": False,
            "id": product_id,
            "name": name,
            "size": size,
            "code": code,
            "weight": weight,
            "stock_quantities": stock_quantities,
            "producer_name": producer_name,
            "product_note": product_note,
            "icons": icons,
        }
        return json.dumps(data, indent=4)

    def _get_product_id(self):
        return self.data["results"][0]["productSkuList"][0].get("productId")

    def _get_name(self):
        return self.data["results"][0]["productSkuList"][0].get("productName")

    def _get_size(self):
        return self.data["results"][0]["productSkuList"][0].get("sizeName")

    def _get_producer_code(self):
        return self.data["results"][0]["productSkuList"][0].get("codeProducer")

    def _get_weight(self):
        weight = self.data["results"][0]["productSkuList"][0].get("weight")
        if weight != 0 or weight is not None:
            weight_kg = "{:.1f}".format(weight / 1000)
        return [
            {"value": weight_kg, "unit": "kg"},
            {"value": weight, "unit": "g"},
        ]

    def _get_stock_quantities(self):
        quantities = []
        for item in self.data["results"][0]["productSkuList"][0].get("quantities", []):
            stock_id = item.get("stockId")
            quantity = item.get("quantity")
            stock_name = STOCK_IDS.get(str(stock_id), "Nieznany")
            quantities.append({"stock_name": stock_name, "quantity": quantity})
        return quantities

    def _get_producer_name(self):
        return self.data["results"][0]["productSkuList"][0].get("producerName")

    def _get_product_note(self):
        return self.data["results"][0]["productSkuList"][0].get("productNote")

    def _get_product_icons(self):
        return {
            "small": self.data["results"][0]["productSkuList"][0]["productIcon"][
                "productIconSmallUrl"
            ],
            "large": self.data["results"][0]["productSkuList"][0]["productIcon"][
                "productIconLargeUrl"
            ],
        }

    def _get_data(self):
        # Implement SKU-specific data retrieval logic
        pass
