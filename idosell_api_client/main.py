import json
from client.product_client import ProductClient
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

    product_json = product_client.get_product("28801-B")
    product_wrapper = JSONParser(product_json)

    product_id = product_wrapper.get_product_id()
    product_names = product_wrapper.get_descriptions("pol")

    print(product_names)


if __name__ == "__main__":
    main()
