class Aggregator:
    def __init__(self):
        # Stores data in the format {stock_code: [(timestamp, total_price), ...]}
        self.data = {}

    def _clean_old_data(self, current_time):
        ten_minutes_ago = current_time - 600  # 600 seconds = 10 minutes
        for stock_code in list(self.data.keys()):
            self.data[stock_code] = [
                entry for entry in self.data[stock_code] if entry[0] > ten_minutes_ago
            ]
            if not self.data[stock_code]:
                del self.data[stock_code]

    def add_data(self, data) -> dict:
        stock_code = data["StockCode"]
        quantity = data["Quantity"]
        price = data["Price"]
        invoice_date = data["InvoiceDate"]
        total_price = quantity * price

        if stock_code not in self.data:
            self.data[stock_code] = []
        self.data[stock_code].append((invoice_date, total_price))

        # Clean old data before calculating the sum
        self._clean_old_data(invoice_date)

        # Calculate the sum for the current stock code
        total_sum = sum(price for _, price in self.data[stock_code])
        return {
            "StockCode": stock_code,
            "Epoch": invoice_date,
            "10minutesSum": total_sum,
        }
