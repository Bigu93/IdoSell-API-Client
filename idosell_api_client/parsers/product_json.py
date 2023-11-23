import json
from .base_json import BaseJSON, error_check
from .size_chart_json import SizeChartJSON


class ProductJSON(BaseJSON):
    @error_check
    def parse(self, lang_ids=None):
        self._validate_lang_ids(lang_ids)
        product_id = self._get_product_id()
        descriptions = json.loads(
            self._get_descriptions(lang_ids)
        )  # Parse JSON string back to a dict
        producer = self._get_producer()
        category = self._get_category()
        displayed_code = self._get_displayed_code()
        product_note = self._get_product_note()
        size_chart_name, size_chart = self._get_size_chart()
        sizes = self._get_sizes()

        data = {
            "error": False,
            "product_id": product_id,
            "displayed_code": displayed_code,
            "category": category,
            "product_note": product_note,
            "producer": producer,
            "sizes": sizes,
            "size_chart_name": size_chart_name,
            "size_chart": size_chart,
            "descriptions": descriptions,
        }

        return json.dumps(data, indent=4)

    @staticmethod
    def _validate_lang_ids(lang_ids):
        if lang_ids is not None:
            if not isinstance(lang_ids, list):
                raise ValueError("Lang IDs must be a list")
            for lang_id in lang_ids:
                if not isinstance(lang_id, str):
                    raise ValueError("Lang IDs must be strings")

    def _get_product_id(self):
        return self.data["results"][0].get("productId")

    def _get_all_product_ids(self):
        return [product.get("productId") for product in self.data.get("results", [])]

    def _get_descriptions(self, lang_ids=None):
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
        return self.data["results"][0].get("producerId"), self.data["results"][0].get(
            "producerName"
        )

    def _get_category(self):
        return self.data["results"][0].get("categoryId"), self.data["results"][0].get(
            "categoryName"
        )

    def _get_displayed_code(self):
        return self.data["results"][0].get("productDisplayedCode")

    def _get_product_note(self):
        return self.data["results"][0].get("productNote")

    def _get_size_chart(self):
        size_chart_name = self.data["results"][0].get("sizeChartName")
        size_chart = SizeChartJSON.get_size_chart_values(size_chart_name)

        return size_chart_name, size_chart

    def _get_sizes(self):
        sizes = self.data["results"][0].get("productSizes")
        data = [size.get("sizePanelName") for size in sizes]

        return data
