import pytest

from wallet.coin.coin import Coin


def test__init__(
    coin_data={"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "amount": 1}
):
    test_coin = Coin(coin_data)

    assert test_coin.id == "bitcoin"
    assert test_coin.symbol == "btc"
    assert test_coin.name == "Bitcoin"
    assert test_coin.amount == 1


def test__str__(
    coin_data={"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "amount": 1}
):
    test_coin = Coin(coin_data)

    assert (
        test_coin.__str__()
        == '{"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "amount": 1}'
    )


def test_fetch_coin_price(
    coin_data={"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "amount": 1}
):
    test_coin = Coin(coin_data)

    test_coin_price = test_coin.fetch_coin_price()

    assert type(test_coin_price) is int
