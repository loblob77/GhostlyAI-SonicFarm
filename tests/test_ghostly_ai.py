from src.ghostly_ai import get_yield_data, optimize_farming
import unittest
from unittest.mock import patch

class TestGhostlyAI(unittest.TestCase):
    @patch("requests.get")
    def test_optimize_farming(self, mock_get):
        mock_get.side_effect = [type("Response", (), {"text": "15.0"})(),
                               type("Response", (), {"text": "10.0"})()]
        yields = get_yield_data()
        self.assertEqual(yields["SwapX"], 15.0)
        self.assertEqual(yields["Silo"], 10.0)
        optimize_farming()  # Just checks it runs

if __name__ == "__main__":
    unittest.main()
