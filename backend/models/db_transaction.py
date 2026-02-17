from sqlalchemy import Column, Integer, String, Float, ForeignKey
from backend.database import Base

class DBTransaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, index=True)
    account_id = Column(String, ForeignKey(accounts.id))
    description = Column(String)
    amount = Column(Float)
    currency = Column(String)
    date = Column(String)
    category = Column(String, nullable=True)