import requests

class Coin:
    exchange_url='https://api.coingecko.com/api/v3/simple/price'

    def __init__(self, id, symbol, name, amount):
        self.id = id
        self.symbol = symbol
        self.name = name
        self.amount = amount
        self.price = self._fetch_price()

    def __str__(self):
        return f'{{"id":"{self.id}","symbol":"{self.symbol}","name":"{self.name}","amount":{self.amount},"price":{self.price}}}'

    def _fetch_price(self):
        price_dict = requests.get(
            self.exchange_url,
            params={
                "ids": self.id,
                "vs_currencies": "eur"}).json()

        token_price = price_dict[self.id]['eur']

        return token_price

