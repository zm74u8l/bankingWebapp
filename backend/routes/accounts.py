from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.db_account import DBAccount

router = APIRouter()

@router.get("/accounts")
def get_accounts(db: Session = Depends(get_db)):
    accounts = db.query(DBAccount).all()
    return accounts

