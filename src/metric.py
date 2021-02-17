class Metric:
    def __init__(self, name, data_type=None, min_val=0, max_val=100):
        self.name = name
        self.data_type = data_type
        self.min_val = min_val
        self.max_val = max_val
