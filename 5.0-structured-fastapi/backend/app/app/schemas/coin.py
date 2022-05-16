from pydantic import BaseModel

from typing import List


class CoinBase(BaseModel):
    coin_id: str
    symbol: str
    name: str
    amount: float


class CoinCreate(CoinBase):
    pass


class CoinUpdate(CoinBase):
    id: int


class CoinInDBBase(CoinBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Coin(CoinInDBBase):
    pass


# Properties properties stored in DB
class CoinInDB(CoinInDBBase):
    pass
