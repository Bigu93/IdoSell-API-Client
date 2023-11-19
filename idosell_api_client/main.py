import json
from client.product_client import ProductClient
from client.sku_client import SKUClient
from client.json_parser import JSONParser
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
    sku_client = SKUClient(BASE_URL, token)

    product_json = sku_client.get_product("28801")
    product_wrapper = JSONParser(product_json)

    product_info = product_wrapper.all_data("")
    print(product_info)


if __name__ == "__main__":
    main()
