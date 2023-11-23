from client.product_client import ProductClient
from client.sku_client import SKUClient
from client.size_chart_client import SizeChartClient
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
    size_chart_client = SizeChartClient(BASE_URL, token)

    product_json = product_client.get_product("28801-B", ["pol", "spa"])
    sku_json = sku_client.get_product("28401-B")
    size_chart_json = size_chart_client.get_size_chart(
        "36-23,5/37-24/38-24,5/39-25/40-25,5/41-26"
    )

    print(product_json)
    print(sku_json)
    print(size_chart_json)


if __name__ == "__main__":
    main()
