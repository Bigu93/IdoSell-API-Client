import json
from .base_json import BaseJSONParser


class ProductJSONParser(BaseJSONParser):
    def parse(self, lang_ids=None):
        product_id = self._get_product_id()
        descriptions = json.loads(
            self._get_descriptions(lang_ids)
        )  # Parse JSON string back to a dict
        producer = self._get_producer()
        category = self._get_category()

        data = {
            "error": False,
            "product_id": product_id,
            "descriptions": descriptions,
            "producer": producer,
            "category": category,
        }

        return json.dumps(data, indent=4)

    def _get_all_product_ids(self):
        if self.has_error:
            return self.error_message

        return [product.get("productId") for product in self.data.get("results", [])]

    def _get_descriptions(self, lang_ids=None):
        if self.has_error:
            return self.error_message

        descriptions = {}
        for description in self.data["results"][0].get(
            "productDescriptionsLangData", []
        ):
            lang = description.get("langId")
            if lang_ids is None or lang in lang_ids:
                descriptions[lang] = {
                    "productName": description.get("productName"),
                    "productLongDescription": description.get("productLongDescription"),
                }

        return json.dumps(descriptions, indent=4)

    def _get_producer(self):
        if self.has_error:
            return self.error_message

        return self.data["results"][0].get("producerId"), self.data["results"][0].get(
            "producerName"
        )

    def _get_category(self):
        if self.has_error:
            return self.error_message

        return self.data["results"][0].get("categoryId"), self.data["results"][0].get(
            "categoryName"
        )
