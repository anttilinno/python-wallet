import yaml
from coin import Coin

class Wallet():
    def __init__(self):
        self.coins = self._load_wallet()
        self.wallet_price = self._calculate_wallet_price()

    def _load_wallet(self):
        coins = []
        try:
            with open("wallet.yaml") as f:
                my_dict = yaml.safe_load(f)
        except FileNotFoundError:
            exit("File not found!")

        for coin in my_dict["coins"]:
            coins.append(Coin(
                coin["id"],
                coin["symbol"],
                coin["name"],
                coin["amount"],
            ));

        return coins

    def _calculate_wallet_price(self):
        wallet_price = 0

        for coin in self.coins:
            wallet_price += coin.price * coin.amount

        return  wallet_price

    def __str__(self):
        return f'Wallet price is {self.wallet_price:.4f}';
