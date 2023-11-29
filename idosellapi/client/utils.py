from typing import List, Dict
from models.product import Product


def create_payload(product_ids: List[Dict] = None, lang_id: str = None) -> Dict:
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
            "resultsPage": 0,
            "resultsLimit": 20,
        }
    }

    if product_ids:
        payload["params"]["productParams"] = [
            {"productId": p_id} for p_id in product_ids
        ]

    if lang_id:
        payload["params"]["productSearchingLangId"] = lang_id

    return payload


def get_nested_attribute(obj, attr_path):
    try:
        for attr in attr_path.split("."):
            if "[" in attr and "]" in attr:
                # Split at '[' and get the index
                attr, index = attr.split("[")
                index = int(index[:-1])  # Remove the ']' and convert to int
                obj = getattr(obj, attr)[index]
            else:
                obj = getattr(obj, attr)
        return obj
    except (AttributeError, IndexError, TypeError):
        return "Not available"


def print_relevant_product_data(product, attributes_dict, width=30):
    # Calculate the total width for the headers based on the specified width
    total_width = width * 2

    separator = "-" * total_width
    header = "---PRODUCT INFO---".center(total_width, "-")

    print(separator)
    print(header)

    for label, attribute in attributes_dict.items():
        if "." in attribute or "[" in attribute:
            value = get_nested_attribute(product, attribute)
        elif hasattr(product, attribute):
            value = getattr(product, attribute)
        else:
            value = "Not available"

        formatted_label = f"{label}: ".ljust(width)
        formatted_value = f"{value}".rjust(width - len(formatted_label))
        print(formatted_label + formatted_value)

    print(separator)
