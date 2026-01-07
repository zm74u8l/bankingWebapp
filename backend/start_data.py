from backend.database import SessionLocal
from backend.models.db_account import DBAccount
from backend.models.db_transaction import DBTransaction
from datetime import date
import uuid

db = SessionLocal()

account = DBAccount(
    id=str(uuid.uuid4()),
    name="Monzo Account",
    type="current"
)

db.add(account)
db.commit()


SessionLocal().add(account)


tx = DBTransaction(
    id=str(uuid.uuid4()),
    account_id=account.id,
    description="Tesco",
    amount=23.50,
    currency="GBP",
    date=date.today(),
    category="Groceries"
)

db.add(tx)
db.commit()

db.close()
print("Sample data inserted")