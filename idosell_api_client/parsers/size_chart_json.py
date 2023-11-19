import json
from .base_json import BaseJSONParser


class SizeChartJSONParser(BaseJSONParser):
    def parse(self, name):
        panel_name = self._get_size_chart()
        if panel_name == name:
            size_chart_values = self.get_size_chart_values(panel_name)
            data = {
                "error": False,
                "message": "Size chart found",
                "size_chart_name": panel_name,
                "size_chart_values": size_chart_values,
            }
        else:
            data = {
                "error": True,
                "message": "Size chart not found",
                "size_chart_name": None,
            }

        return json.dumps(data, indent=4)

    def check_for_errors(self):
        error_info = self.data.get("errors", {})
        fault_code = error_info.get("faultCode")
        fault_string = error_info.get("faultString")

        if fault_code != 0 or fault_string:
            self.has_error = True
            return {"error": True, "message": fault_string, "code": fault_code}

        if not self.data.get("sizeCharts"):
            self.has_error = True
            return {"error": True, "message": "No results found", "code": -1}

        return {"error": False}

    def _get_size_chart(self):
        if self.has_error:
            return self.error_message

        size_charts = list(self.data["sizeCharts"].values())

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
