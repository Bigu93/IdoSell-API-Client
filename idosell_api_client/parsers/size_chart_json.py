import json
from .base_json import BaseJSON, error_check


class SizeChartJSON(BaseJSON):
    def __init__(self, json_data, name):
        super().__init__(json_data, result_key="sizeCharts")
        self.name = name
        self.path = self.get_path()

    @error_check
    def parse(self):
        panel_name = self._get_size_chart()
        if panel_name == self.name:
            size_chart_values = self.get_size_chart_values(panel_name)
            self.parsed_data = {
                "error": False,
                "message": "Size chart found",
                "size_chart_name": panel_name,
                "size_chart_values": size_chart_values,
            }
        else:
            self.parsed_data = {
                "error": True,
                "message": "Size chart not found",
                "size_chart_name": None,
            }

        return self.parsed_data

    def get_path(self):
        pass

    def _get_size_chart(self):
        size_charts = list(self.data[self.result_key].values())
        return size_charts[0].get("nameInPanel", None)

    @staticmethod
    def get_size_chart_values(size_chart_name):
        if not size_chart_name or not isinstance(size_chart_name, str):
            raise ValueError("Invalid chart string format.")

        parts = size_chart_name.split("/")
        is_grouped = any("-" not in part for part in parts)

        if is_grouped:
            pairs = [
                (parts[i] + "/" + parts[i + 1]).split("-")
                for i in range(0, len(parts), 2)
            ]
        else:
            pairs = [part.split("-") for part in parts]

        chart_values = {size: value for size, value in pairs}

        return chart_values
