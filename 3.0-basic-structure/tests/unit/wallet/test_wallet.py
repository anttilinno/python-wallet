import pytest
import unittest
import re

from wallet.wallet import Wallet
from wallet.coin.coin import Coin

test_yaml_file = "data/test_wallet.yaml"

def test__init__():
    test_wallet = Wallet(test_yaml_file)
    assert type(test_wallet) is Wallet


def test__str__():
    test_wallet = Wallet(test_yaml_file)

    assert (
        type(re.match(r"^Wallet value is: \d+ €$", test_wallet.__str__())) is re.Match
    )


def test_load_yaml():
    test_wallet = Wallet(test_yaml_file)

    assert test_wallet.wallet_from_yaml == {
        "coins": [{"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "amount": 1}]
    }


def test_populate_wallet():
    test_wallet = Wallet(test_yaml_file)

    [coin_in_wallet] = test_wallet._populate_wallet()

    assert type(coin_in_wallet) is Coin
    # This is not best practice
    assert (
        coin_in_wallet.__dict__
        == Coin(
            {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "amount": 1}
        ).__dict__
    )


def test_calculate_value():
    test_wallet = Wallet(test_yaml_file)

    [coin_in_wallet] = test_wallet._populate_wallet()

    coin_price = coin_in_wallet.fetch_coin_price()

    test_wallet_value = test_wallet._calculate_value()

    assert coin_price == test_wallet_value
