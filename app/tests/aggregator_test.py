import unittest

from aggregator import Aggregator


class TestAggregator(unittest.TestCase):
    def test_aggregate(self):
        """
        Test the aggregated calculation of a given invoice
        """
        data = {
            "Invoice": "489574",
            "StockCode": "21491",
            "Description": "SET OF THREE VINTAGE GIFT WRAPS",
            "Quantity": 2,
            "Price": 1.95,
            "Customer ID": 13097.0,
            "Country": "United Kingdom",
            "InvoiceDate": 1674744306.978004,
        }
        expected = {
            "StockCode": "21491",
            "Epoch": 1674744306.978004,
            "10minutesSum": 3.9,
        }
        result = Aggregator().add_data(data=data)
        print(result)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
