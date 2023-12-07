def create_payload(product_ids: list[dict] = None, lang_id: str = None) -> dict:
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
