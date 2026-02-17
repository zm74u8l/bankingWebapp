from fastapi import FastAPI
from backend.routes.accounts import router as accounts_router
from backend.routes.transactions import router as transactions_router
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.routes.chat import router as chat_router
#from banking_app.routes import accounts, transactions, users

app = FastAPI()
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "My app"}


app.include_router(accounts_router)
app.include_router(transactions_router)