import os
import sys
from unittest.mock import patch, MagicMock

# Allow importing from the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.trading_bot import get_price, TradingBot


@patch("src.trading_bot.requests.get")
def test_get_price(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": {"amount": "12345.67"}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    price = get_price("BTC-USD")

    assert price == 12345.67
    mock_get.assert_called_once()


@patch("src.trading_bot.get_price")
def test_trading_bot_decision(mock_get_price):
    mock_get_price.side_effect = [100.0, 110.0]
    bot = TradingBot(window=2)

    # First price just populates history
    price1 = bot.fetch_price()
    assert price1 == 100.0
    assert bot.decide_action() == "hold"

    # Second price triggers a sell signal since 110 > average 105
    price2 = bot.fetch_price()
    assert price2 == 110.0
    assert bot.decide_action() == "sell"
