from sqlalchemy import Column, Integer, String, Float
from backend.database import Base

class DBAccount(Base):
    __tablename__ = "accounts"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    amount = Column(String)
    currency = Column(Float)
