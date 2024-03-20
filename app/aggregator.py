class Aggregator:
    def __init__(self):
        # Stores data in the format {stock_code: [(timestamp, total_price), ...]}
        self.data = {}

    def add_data(self, data) -> dict:
        pass