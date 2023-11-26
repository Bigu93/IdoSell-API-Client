import json
from .base_json import BaseJSON, error_check
from .size_chart_json import SizeChartJSON


class ProductJSON(BaseJSON):
    def __init__(self, json_data, lang_ids=None):
        super().__init__(json_data)
        self.path = self.get_path()
        if self.has_error:
            self.error_message
        else:
            pass

    @error_check
    def parse(self, lang_ids=None):
        self._validate_lang_ids(lang_ids)
        self.parsed_data = {
            "error": False,
            "product_id": self._get_product_id(),
            "displayed_code": self._get_displayed_code(),
            "category": self._get_category(),
            "sizes": self._get_sizes(),
            "size_chart_name": self._get_size_chart()[0],
            "size_chart": self._get_size_chart()[1],
            "descriptions": self._get_descriptions(lang_ids),
        }

        return self.parsed_data

    @error_check
    def parse_all(self, lang_ids=None):
        self._validate_lang_ids(lang_ids)
        all_products_data = self.data.get("results", [])

        parsed_products = []
        for product_data in all_products_data:
            self.path = product_data
            parsed_product = {
                "product_id": self._get_product_id(),
                "displayed_code": self._get_displayed_code(),
                "category": self._get_category(),
                "sizes": self._get_sizes(),
                "size_chart_name": self._get_size_chart()[0],
                "size_chart": self._get_size_chart()[1],
                "descriptions": self._get_descriptions(lang_ids),
            }
            parsed_products.append(parsed_product)

        self.parsed_data = {
            "error": False,
            "products": parsed_products,
        }

    @staticmethod
    def _validate_lang_ids(lang_ids):
        if lang_ids is not None:
            if not isinstance(lang_ids, list):
                raise ValueError("Lang IDs must be a list")
            for lang_id in lang_ids:
                if not isinstance(lang_id, str):
                    raise ValueError("Lang IDs must be strings")

    def get_path(self):
        return self.data[self.result_key][0]

    def _get_product_id(self):
        return self.path.get("productId")

    def _get_all_product_ids(self):
        return [product.get("productId") for product in self.data.get("results", [])]

    def _get_descriptions(self, lang_ids=None):
        descriptions = {}
        for description in self.path.get("productDescriptionsLangData", []):
            lang = description.get("langId")
            if lang_ids is None or lang in lang_ids:
                descriptions[lang] = {
                    "productName": description.get("productName"),
                    "productLongDescription": description.get("productLongDescription"),
                }

        return descriptions

    def _get_category(self):
        return self.path.get("categoryId"), self.path.get("categoryName")

    def _get_displayed_code(self):
        return self.path.get("productDisplayedCode")

    def _get_product_note(self):
        return self.path.get("productNote")

    def _get_size_chart(self):
        size_chart_name = self.path.get("sizeChartName")
        size_chart = SizeChartJSON.get_size_chart_values(size_chart_name)

        return size_chart_name, size_chart

    def _get_sizes(self):
        sizes = self.path.get("productSizes")
        data = [size.get("sizePanelName") for size in sizes]

        return data
