from typing import List
from pydantic import BaseModel, HttpUrl

from coin import Coin


class Wallet(BaseModel):
    label: str
    coins: List[Coin]
