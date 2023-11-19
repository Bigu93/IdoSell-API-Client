class APIError(Exception):
    def __init__(self, message, fault_code=None):
        self.message = message
        self.fault_code = fault_code
        super().__init__(self.message)

    def __str__(self):
        if self.fault_code is not None:
            return f"APIError {self.fault_code}: {self.message}"
        else:
            return f"APIError: {self.message}"
