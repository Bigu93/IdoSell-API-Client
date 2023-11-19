import json
from .base_json import BaseJSONParser


class SizeChartJSONParser(BaseJSONParser):
    def parse(self, name):
        panel_name = self._get_size_chart()
        if panel_name == name:
            return {
                "error": False,
                "message": "Size chart found",
                "size_chart_name": panel_name,
            }
        else:
            return {
                "error": True,
                "message": "Size chart not found",
                "size_chart_name": None,
            }

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
