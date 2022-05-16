from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Coin])
def read_coins(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve coins.
    """
    coins = crud.coin.get_multi(db, skip=skip, limit=limit)
    return coins


@router.post("/", response_model=schemas.Coin)
def create_coin(
    *, db: Session = Depends(deps.get_db), coin_in: schemas.CoinCreate
) -> Any:
    """
    Create new coin.
    """
    coin = crud.coin.create(db=db, obj_in=coin_in)
    return coin


@router.put("/{id}", response_model=schemas.Coin)
def update_coin(
    *, db: Session = Depends(deps.get_db), id: int, coin_in: schemas.CoinUpdate
) -> Any:
    """
    Update an coin.
    """
    coin = crud.coin.get(db=db, id=id)
    if not coin:
        raise HTTPException(status_code=404, detail="Coin not found")

    coin = crud.coin.update(db=db, db_obj=coin, obj_in=coin_in)
    return coin


@router.get("/{id}", response_model=schemas.Coin)
def read_coin(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """
    Get coin by ID.
    """
    coin = crud.coin.get(db=db, id=id)
    if not coin:
        raise HTTPException(status_code=404, detail="Item not found")
    return coin


@router.delete("/{id}", response_model=schemas.Coin)
def delete_coin(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """
    Delete an coin.
    """
    coin = crud.coin.get(db=db, id=id)
    if not coin:
        raise HTTPException(status_code=404, detail="Coin not found")
    coin = crud.coin.remove(db=db, id=id)
    return coin
