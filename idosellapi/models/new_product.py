class APIResponse:
    def __init__(self, results_limit, errors, results):
        self.results_limit = results_limit
        self.errors = errors
        self.results = results

    def is_successful(self):
        return not self.errors and len(self.results) > 0


class ErrorDetail:
    def __init__(self, fault_code, fault_string):
        self.fault_code = fault_code
        self.fault_string = fault_string

