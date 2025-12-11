from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    account_id: str
    description: str
    amount: float
    currency: str
    date: str
    category: str | None = None