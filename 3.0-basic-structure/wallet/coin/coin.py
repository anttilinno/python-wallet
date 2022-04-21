import requests


class Coin:
    """Coin"""

    exchange_url = "https://api.coingecko.com/api/v3/simple/price"

    def __init__(self, coin_data):
        self.id, self.symbol, self.name, self.amount = list(coin_data.values())

    def __str__(self):
        return f"{{id: {self.id}, symbol: {self.symbol}, name: {self.name}, amount: {self.amount}}}"

    def fetch_coin_price(self):
        """Fetch coin price from exchange_url"""

        price_dict = requests.get(
            self.exchange_url, params={"ids": self.id, "vs_currencies": "eur"}
        ).json()

        return price_dict[self.id]["eur"]
