import json


class JSONParser:
    def __init__(self, json_data):
        self.data = json_data

    def get_all_product_ids(self):
        return [product.get("productId") for product in self.data.get("results", [])]

    def get_product_id(self):
        return {"id": self.data["results"][0].get("productId")}

    def get_descriptions(self, lang_id=None):
        descriptions = {}
        for description in self.data["results"][0].get(
            "productDescriptionsLangData", []
        ):
            lang = lang_id or description.get("langId")
            descriptions[lang] = {
                "productName": description.get("productName"),
                "productLongDescription": description.get("productLongDescription"),
            }
        return json.dumps(descriptions, indent=4)

    def get_producer(self):
        return {
            "id": self.data["results"][0].get("producerId"),
            "name": self.data["results"][0].get("producerName"),
        }

    def get_category(self):
        return {
            "id": self.data["results"][0].get("categoryId"),
            "name": self.data["results"][0].get("categoryName"),
        }

    def compile_all_data(self, lang_id=None):
        product_id = self.get_product_id()
        descriptions = json.loads(
            self.get_descriptions(lang_id)
        )  # Parse JSON string back to a dict
        producer = self.get_producer()
        category = self.get_category()

        compiled_data = {
            "productId": product_id,
            "descriptions": descriptions,
            "producer": producer,
            "category": category,
        }

        return json.dumps(compiled_data, indent=4)
