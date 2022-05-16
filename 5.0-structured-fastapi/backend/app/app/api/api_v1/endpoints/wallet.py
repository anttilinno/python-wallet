from typing import Any, Optional, List

from fastapi import APIRouter, Depends, HTTPException

from app import crud, models, schemas
from app.api import deps
from app.schemas.wallet import Wallet

router = APIRouter()


@router.get("/", response_model=Wallet)
def fetch_wallet() -> Wallet:
    """
    Fetch wallet and show it
    """

    wallet = Wallet(label="Test wallet")

    return wallet
