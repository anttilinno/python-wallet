from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.coin import Coin
from app.schemas.coin import CoinCreate, CoinUpdate


class CRUDCoin(CRUDBase[Coin, CoinCreate, CoinUpdate]):
    pass


coin = CRUDCoin(Coin)
