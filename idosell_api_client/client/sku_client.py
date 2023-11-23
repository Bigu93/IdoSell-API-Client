from .base_client import BaseClient
from parsers.sku_json import SkuJSON


class SKUClient(BaseClient):
    def __init__(self, base_url, auth_token):
        super().__init__(base_url, auth_token)

    def get_product(self, product_id):
        response = self.get(
            f"api/admin/v1/products/SKUbyBarcode?productIndices={product_id}"
        )
        parser = SkuJSON(response)
        return parser.parse()
