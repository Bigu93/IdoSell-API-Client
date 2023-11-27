from client.base_client import BaseClient
from client.product_api import ProductApi
from models.response import process_response
from config.settings import (
    BASE_URL,
    CLIENT_SECRET,
    CLIENT_USERNAME,
)
from client.auth import Auth
from client.utils import create_payload


def main():
    auth = Auth(CLIENT_USERNAME, CLIENT_SECRET, BASE_URL)
    token = auth.get_token()

    products = ProductApi(BASE_URL, token)

    product_ids = [21000, 21001, 21002, 28676]
    lang_id = "pol"

    payload = create_payload(product_ids, lang_id)
    response = products.get_products(payload)
    processed_response = process_response(response.data)

    product_info = [processed_response]
    for product in product_info[0].results:
        print(product.product_id)


if __name__ == "__main__":
    main()
