import json


class JSONParser:
    def __init__(self, json_data):
        self.data = json_data

    def get_product_details(self, product_id):
        for product in self.data.get("results", []):
            if product.get("productId") == product_id:
                return {
                    "id": product.get("productId"),
                    "name": product.get("productName"),
                    "price": product.get("productRetailPrice"),
                    "producer": product.get("producerName"),
                    "category": product.get("categoryName"),
                }
        return None

    def get_all_product_ids(self):
        return [product.get("productId") for product in self.data.get("results", [])]

    def get_stock_info(self, product_id):
        for product in self.data.get("results", []):
            if product.get("productId") == product_id:
                return product.get("productStocksData", [])
        return None
