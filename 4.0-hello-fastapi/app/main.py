import httpx

from fastapi import FastAPI, APIRouter
from typing import Any
from yaml import load
from yaml import CLoader as Loader


app = FastAPI(title="FastAPI simple wallet API")

api_router = APIRouter()


async def fetch_and_calculate_wallet_value() -> int:
    """Fetch coin price from Coingecko and sum wallet value"""

    with open(r"data/wallet.yaml") as file:
        wallet: Any = load(file, Loader=Loader)

    exchange_url = "https://api.coingecko.com/api/v3/simple/price"

    coin_ids = ",".join([coin["id"] for coin in wallet["coins"]])

    async with httpx.AsyncClient() as client:
        r = await client.get(
            exchange_url, params={"ids": coin_ids, "vs_currencies": "eur"}
        )

    return sum(coin_price["eur"] for coin_price in r.json().values())


@api_router.get("/", status_code=200)
async def get_wallet_value() -> int:
    """
    Get wallet value from Coingecko
    """

    wallet_value = await fetch_and_calculate_wallet_value()

    return wallet_value


app.include_router(api_router)
