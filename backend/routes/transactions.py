from fastapi import APIRouter, Depends, UploadFile, File
import csv
import io
import uuid
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.db_transaction import DBTransaction
from backend.models.transaction import Transaction
from datetime import date

router = APIRouter()

@router.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(DBTransaction).all()
    return transactions

@router.post("/transactions/upload-csv")
def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = file.file.read().decode("utf-8")
    csv_read = csv.DictReader(io.StringIO(content))

    inserted_transactions = 0
    for row in csv_read:
        transaction = DBTransaction(
            id=str(uuid.uuid4()),
            account_id=row["account_id"],
            description=row["description"],
            amount=float(row["amount"]),
            currency=row["currency"],
            date=date.fromisoformat(row["date"]),
            category=row["category"]
        )
        db.add(transaction)
        inserted_transactions += 1

    db.commit()
    return {"message": f"{inserted_transactions} transactions inserted successfully."}


@router.post("/transactions")
def create_transaction(transaction: Transaction, db: Session = Depends(get_db)):
    db_transaction = DBTransaction(
        id=transaction.id,
        account_id=transaction.account_id,
        description=transaction.description,
        amount=transaction.amount,
        currency=transaction.currency,
        date=date.fromisoformat(transaction.date),
        category=transaction.category
    )
    db.add(db_transaction)
    db.commit()
    return {"message": "Transaction created successfully"}