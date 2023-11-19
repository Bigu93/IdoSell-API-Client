from .base_client import BaseClient


class SKUClient(BaseClient):
    def __init__(self, base_url, auth_token):
        super().__init__(base_url, auth_token)

    def get_product(self, product_id):
        return self.get(f"api/admin/v1/products/products?productIds={product_id}")

    def add_product(self, product_data):
        return self.post("products", data=product_data)

    def update_product(self, product_id, product_data):
        return self.put(f"products/{product_id}", data=product_data)

    def delete_product(self, product_id):
        return self.delete(f"products/{product_id}")
