from .base_client import BaseClient
from parsers.size_chart_json import SizeChartJSONParser


class SizeChartClient(BaseClient):
    def __init__(self, base_url, auth_token):
        super().__init__(base_url, auth_token)

    def get_size_chart(self, size_chart_name):
        response = self.get(
            f"api/admin/v1/sizecharts/sizecharts?names={size_chart_name}"
        )
        parser = SizeChartJSONParser(response)
        return parser.parse(size_chart_name)