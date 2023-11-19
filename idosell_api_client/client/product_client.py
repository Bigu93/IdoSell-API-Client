from .base_client import BaseClient
from parsers.product_json import ProductJSONParser


class ProductClient(BaseClient):
    def __init__(self, base_url, auth_token):
        super().__init__(base_url, auth_token)

    def get_product(self, product_id, lang_id=None):
        response = self.get(f"api/admin/v1/products/products?productIds={product_id}")
        parser = ProductJSONParser(response)
        return parser.parse(lang_id)

    def add_product(self, product_data):
        # TODO - implement product data validation
        return self.post("products", data=product_data)

    def update_product(self, product_id, product_data):
        # TODO - implement product data validation
        return self.put(f"products/{product_id}", data=product_data)

    def delete_product(self, product_id):
        # TODO - implement product data validation
        return self.delete(f"products/{product_id}")
