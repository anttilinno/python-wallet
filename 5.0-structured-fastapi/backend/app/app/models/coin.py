from sqlalchemy import Column, String, BigInteger, Float

from app.db.base_class import Base


class Coin(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    coin_id = Column(String)
    symbol = Column(String, index=True)
    name = Column(String)
    amount = Column(Float)
