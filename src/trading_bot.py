import requests


def get_price(symbol="BTC-USD"):
    """Fetch the spot price for a given symbol from Coinbase."""
    url = f"https://api.coinbase.com/v2/prices/{symbol}/spot"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return float(data["data"]["amount"])


def main():
    price = get_price()
    print(f"Current BTC price in USD: ${price:.2f}")


if __name__ == "__main__":
    main()
