import json
from .base_json import BaseJSONParser
from config.settings import STOCK_IDS


class SKUJSONParser(BaseJSONParser):
    def parse(self):
        product_id = self._get_product_id()
        name = self._get_name()
        producer_code = self._get_producer_code()
        weight = self._get_weight()
        stock_quantities = self._get_stock_quantities()

        data = {
            "id": product_id,
            "name": name,
            "producer_code": producer_code,
            "weight": weight,
            "stock_quantities": stock_quantities,
        }
        return json.dumps(data, indent=4)

    def _get_product_id(self):
        if self.has_error:
            return self.error_message
        return self.data["results"][0]["productSkuList"][0].get("productId")

    def _get_name(self):
        if self.has_error:
            return self.error_message
        return self.data["results"][0]["productSkuList"][0].get("productName")

    def _get_producer_code(self):
        if self.has_error:
            return self.error_message
        return self.data["results"][0]["productSkuList"][0].get("codeProducer")

    def _get_weight(self):
        if self.has_error:
            return self.error_message
        weight = self.data["results"][0]["productSkuList"][0].get("weight")
        if weight != 0 or weight is not None:
            weight_kg = "{:.1f}".format(weight / 1000)
        return [
            {"value": weight_kg, "unit": "kg"},
            {"value": weight, "unit": "g"},
        ]

    def _get_stock_quantities(self):
        if self.has_error:
            return self.error_message
        quantities = []
        for item in self.data["results"][0]["productSkuList"][0].get("quantities", []):
            stock_id = item.get("stockId")
            quantity = item.get("quantity")
            stock_name = STOCK_IDS.get(str(stock_id), "Nieznany")
            quantities.append({"stock_name": stock_name, "quantity": quantity})
        return quantities

    def _get_data(self):
        # Implement SKU-specific data retrieval logic
        pass
