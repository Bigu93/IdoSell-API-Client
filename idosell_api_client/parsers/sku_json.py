from .base_json import BaseJSON, error_check
from client.utils import parse_location
from config.settings import STOCK_IDS


class SkuJSON(BaseJSON):
    def __init__(self, json_data):
        super().__init__(json_data)
        if not self.has_error:
            self.product_id = self._get_product_id()
            self.name = self._get_name()
            self.size = self._get_size()
            self.code = self._get_producer_code()
            self.weight = self._get_weight()
            self.locations = self._get_stock_locations()
            self.stock_quantities = self._get_stock_quantities()
            self.producer_name = self._get_producer_name()
            self.product_note = self._get_product_note()
            self.icons = self._get_product_icons()
        else:
            self.error_message

    @error_check
    def parse(self):
        self.parsed_data = {
            "error": False,
            "id": self.product_id,
            "name": self.name,
            "size": self.size,
            "code": self.code,
            "weight": self.weight,
            "locations": self.locations,
            "stock_quantities": self.stock_quantities,
            "producer_name": self.producer_name,
            "product_note": self.product_note,
            "icons": self.icons,
        }
        return self.parsed_data

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

    def _get_stock_locations(self):
        locations = []
        for item in self.data["results"][0]["productSkuList"][0].get(
            "stockLocations", []
        ):
            stock_id = item.get("stockId")
            stock_location_id = item.get("stockLocationId")
            stock_location_text = parse_location(item.get("stockLocationTextId"))
            stock_name = STOCK_IDS.get(str(stock_id), "Nieznany")
            locations.append(
                {
                    "stock_location_id": stock_location_id,
                    "stock_name": stock_name,
                    "location": stock_location_text,
                }
            )
        return locations

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
