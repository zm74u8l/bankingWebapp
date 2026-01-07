from backend.database import Engine, Base
from backend.models.db_account import DBAccount
from backend.models.db_transaction import DBTransaction

Base.metadata.create_all(bind=Engine)
print("Tables created successfully.")