import os
import sys
from unittest.mock import patch, MagicMock

# Allow importing from the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.trading_bot import get_price


@patch("src.trading_bot.requests.get")
def test_get_price(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": {"amount": "12345.67"}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    price = get_price("BTC-USD")

    assert price == 12345.67
    mock_get.assert_called_once()
