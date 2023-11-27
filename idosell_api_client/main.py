from client.base_client import BaseClient
from models.product import (
    Authenticate,
    Errors,
    ProductAuctionIcon,
    ProductDescriptionsLangDatum,
    ProductDiscount,
    ProductIcon,
    ProductImage,
    ProductIndividualDescriptionsDatum,
    ProductParametersDistinction,
    ProductSize,
    URLLangDatum,
    Result,
    Product,
)
from config.settings import (
    BASE_URL,
    CLIENT_SECRET,
    CLIENT_USERNAME,
)
from client.auth import Auth


def main():
    auth = Auth(CLIENT_USERNAME, CLIENT_SECRET, BASE_URL)
    token = auth.get_token()

    idosellapi = BaseClient(BASE_URL, token)
    payload = {
        "params": {
            "returnProducts": "active",
            "returnElements": [
                "code",
                "note",
                "category_name",
                "retail_price",
                "wholesale_price",
                "minimal_price",
                "pos_price",
                "strikethrough_retail_price",
                "last_purchase_price",
                "weight",
                "complex_notes",
                "traits",
                "discount",
                "icon",
                "icon_for_auctions",
                "pictures",
                "sizeschart_name",
                "sizes",
                "new_product",
                "lang_data",
                "productIndividualDescriptionsData",
            ],
            "productParams": [{"productId": 21000}],
            "resultsPage": 0,
            "resultsLimit": 20,
            "productSearchingLangId": "pol",
        }
    }

    response = idosellapi.post("products/products/get", data=payload)

    # Parse the authentication and errors data
    product_info = []
    authenticate = Authenticate(**response.data["authenticate"])
    errors = Errors(**response.data["errors"])

    # Create Result instances for each product in the results array
    results = [Result(**product_data) for product_data in response.data["results"]]

    # Create the Product instance
    product = Product(
        authenticate=authenticate,
        resultsPage=response.data["resultsPage"],
        resultsLimit=response.data["resultsLimit"],
        resultsNumberPage=response.data["resultsNumberPage"],
        resultsNumberAll=response.data["resultsNumberAll"],
        errors=errors,
        results=results,
    )

    product_info.append(product)
    print(product_info[0].resultsNumberAll)


if __name__ == "__main__":
    main()
