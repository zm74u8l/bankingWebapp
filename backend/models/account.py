from pydantic import BaseModel

class Account(BaseModel):
    id: str
    name: str
    total: float
    currency: str
    type: str