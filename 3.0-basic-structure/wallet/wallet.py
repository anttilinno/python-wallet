# Try to use C loader first
try:
    from yaml import load, CFullLoader as FullLoader
except ImportError:
    from yaml import load, FullLoader

from .coin.coin import Coin


class Wallet:
    """Wallet object, with helpers for loading the content from YAML file and
    calculating the wallet current value.
    """

    def __init__(self, yaml_file="data/wallet.yaml"):
        self.yaml_file = yaml_file
        self._load_yaml()
        self.coins = self._populate_wallet()
        self.wallet_value = self._calculate_value()

    def __str__(self):
        return f"Wallet value is: {self.wallet_value} €"

    def _load_yaml(self):
        with open(self.yaml_file, mode="rt", encoding="utf-8") as file:
            self.wallet_from_yaml = load(file, FullLoader)

    def _populate_wallet(self):
        return [Coin(x) for x in self.wallet_from_yaml["coins"]]

    def _calculate_value(self):
        wallet_value = 0

        for coin in self.coins:
            wallet_value += coin.amount * coin.fetch_coin_price()

        return wallet_value
