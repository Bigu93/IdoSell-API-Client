from idosellapi.client.product_api import ProductApi
from idosellapi.exceptions.api_exceptions import ProductInfoError, NoProductFoundError
from idosellapi.config.settings import (
    BASE_URL,
    CLIENT_SECRET,
    CLIENT_USERNAME,
)
from idosellapi.client.auth import Auth
from idosellapi.client.utils import create_payload


class ProductData:
    def __init__(self):
        self.auth = Auth(CLIENT_USERNAME, CLIENT_SECRET, BASE_URL)
        self.token = self.auth.get_token()
        self.products = ProductApi(BASE_URL, self.token)

    def get_product_info(self, product_id, lang_id="pol"):
        payload = create_payload(product_id, lang_id)
        response = self.products.get_products(payload)

        if response.status_code != 200:
            raise ProductInfoError("Error while getting product info")
        if response.data:
            if response.data["resultsNumberAll"] == 0:
                raise NoProductFoundError("Brak takiego produktu w bazie")

            product_info = response.data
            return product_info["results"][0]


# def main():
#     auth = Auth(CLIENT_USERNAME, CLIENT_SECRET, BASE_URL)
#     token = auth.get_token()

#     products = ProductApi(BASE_URL, token)

#     product_ids = [21002, 21003, 23643, 25000, 26000, 27000]
#     lang_id = "pol"

#     payload = create_payload(product_ids, lang_id)
#     response = products.get_products(payload)
#     processed_response = process_response(response.data)

#     product_info = [processed_response]
#     return product_info[0].results[0]
# print(product_info[0].results[0].id)
# attributes_to_print = {
#     "Product ID": "id",
#     "Product Name": "descriptions_lang_data[0].product_name",
#     "Product Price": "retail_price",
# }

# for product in product_info[0].results:
#     print_relevant_product_data(product, attributes_to_print)


# if __name__ == "__main__":
#     main()
