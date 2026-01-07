from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class DBTransaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, index=True)
    account_id = Column(String, index = True)
    description = Column(String)
    amount = Column(Float)
    currency = Column(String)
    date = Column(String)
    category = Column(String, nullable=True)