class APIError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"APIError: {self.message}"


# Example Usage
# raise APIError("Invalid response from the API")
