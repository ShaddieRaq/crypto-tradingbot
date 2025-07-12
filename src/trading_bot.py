import requests
from collections import deque


def get_price(symbol: str = "BTC-USD") -> float:
    """Fetch the spot price for a given symbol from Coinbase."""
    url = f"https://api.coinbase.com/v2/prices/{symbol}/spot"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return float(data["data"]["amount"])


class TradingBot:
    """A very small trading bot that uses a moving average strategy."""

    def __init__(self, symbol: str = "BTC-USD", window: int = 5) -> None:
        self.symbol = symbol
        self.prices: deque[float] = deque(maxlen=window)

    def fetch_price(self) -> float:
        """Fetch the latest price and store it."""
        price = get_price(self.symbol)
        self.prices.append(price)
        return price

    def moving_average(self) -> float:
        return sum(self.prices) / len(self.prices) if self.prices else 0.0

    def decide_action(self) -> str:
        if not self.prices:
            return "hold"
        price = self.prices[-1]
        avg = self.moving_average()
        if price < avg:
            return "buy"
        if price > avg:
            return "sell"
        return "hold"


def main() -> None:
    bot = TradingBot()
    price = bot.fetch_price()
    action = bot.decide_action()
    avg = bot.moving_average()
    print(f"Price: ${price:.2f} | Avg: ${avg:.2f} -> {action}")


if __name__ == "__main__":
    main()
