import json
from client.product_client import ProductClient
from client.sku_client import SKUClient
from parsers.product_json import ProductJSONParser
from config.settings import (
    BASE_URL,
    CLIENT_SECRET,
    CLIENT_USERNAME,
)
from client.auth import Auth


def main():
    auth = Auth(CLIENT_USERNAME, CLIENT_SECRET, BASE_URL)
    token = auth.get_token()

    product_client = ProductClient(BASE_URL, token)
    # sku_client = SKUClient(BASE_URL, token)

    product_json = product_client.get_product("28801-B")
    product_wrapper = ProductJSONParser(product_json)

    product_info = product_wrapper.parse("spa")
    print(product_info)


if __name__ == "__main__":
    main()
