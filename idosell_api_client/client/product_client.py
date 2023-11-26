from .base_client import BaseClient
from parsers.product_json import ProductJSON


class ProductClient(BaseClient):
    def __init__(self, base_url, auth_token):
        super().__init__(base_url, auth_token)

    def get_product(self, product_ids, lang_ids=None):
        self._validate_product_id(product_ids)
        response = self.get(
            f"api/admin/v1/products/products?productIds={','.join(map(str, product_ids))}"
        )
        parser = ProductJSON(response, lang_ids)
        if product_ids and len(product_ids) > 1:
            parser.parse_all(lang_ids)
        else:
            parser.parse()
        return parser

    def add_product(self, product_data):
        # TODO - implement product data validation
        return self.post("products", data=product_data)

    def update_product(self, product_ids, product_data):
        # TODO - implement product data validation
        return self.put(f"products/{product_ids}", data=product_data)

    def delete_product(self, product_ids):
        # TODO - implement product data validation
        return self.delete(f"products/{product_ids}")

    @staticmethod
    def _validate_product_id(product_ids):
        if not product_ids:
            return False
        if not isinstance(product_ids, list):
            raise ValueError("Product ID must be a list of strings")
