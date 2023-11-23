from .base_client import BaseClient
from parsers.product_json import ProductJSON


class ProductClient(BaseClient):
    def __init__(self, base_url, auth_token):
        super().__init__(base_url, auth_token)

    def get_product(self, product_id, lang_ids=None):
        self._validate_product_id(product_id)
        response = self.get(f"api/admin/v1/products/products?productIds={product_id}")
        parser = ProductJSON(response, lang_ids)
        return parser.parse()

    def add_product(self, product_data):
        # TODO - implement product data validation
        return self.post("products", data=product_data)

    def update_product(self, product_id, product_data):
        # TODO - implement product data validation
        return self.put(f"products/{product_id}", data=product_data)

    def delete_product(self, product_id):
        # TODO - implement product data validation
        return self.delete(f"products/{product_id}")

    @staticmethod
    def _validate_product_id(product_id):
        if not product_id:
            raise ValueError("Product ID cannot be empty")
        if not isinstance(product_id, str):
            raise ValueError("Product ID must be a string")
