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

    product_id = product_client.get_product("48-B")
    product_details = JSONParser(product_id)
    print(product_details.get_all_product_ids())


if __name__ == "__main__":
    main()
