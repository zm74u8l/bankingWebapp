from datetime import date
from sqlalchemy.orm import Session
from backend.models.db_transaction import DBTransaction
from backend.routes.transactions import get_transactions
from collections import defaultdict
from datetime import timedelta, date


def total_spend(db: Session):
    return(
        db.query(DBTransaction)
        .filter(DBTransaction.amount < 0)
        .with_entities(DBTransaction.amount)
        .all()
    )

def max_transaction(db: Session):
    return (
        db.query(DBTransaction)
        .order_by(DBTransaction.amount.asc())
        .first()

    )

def all_transactions(db:Session):
    return(
        db.query(DBTransaction)
        .order_by(DBTransaction.date.desc())
        .all()
    )

def subscriptions(timeframe: int, db, latest_date: date = date.today()):
    #can allow for yearly subscriptions
    groups = defaultdict(list)
    transactions = all_transactions(db)
    if timeframe >36:
        for transaction in transactions:
            if transaction.amount < 0:
                key = (transaction.description.lower(), round(transaction.amount,2))
                groups[key].append(transaction)
        subscriptions = []
        print(groups.items())
        for key, recurring in groups.items():
            if len(recurring) > 2:
                recurring = sorted(recurring, key=lambda x: x.date)
                print(type(recurring[0].date), recurring[0].date)


                intervals = [
                    (date.fromisoformat(recurring[i].date) - date.fromisoformat(recurring[i - 1].date)).days
                    for i in range(1, len(recurring))
                ]

                avg_interval = sum(intervals) / len(intervals)
                if 360 <= avg_interval <= 370:
                    subscriptions.append({
                        "description": key[0],
                        "amount": key[1],
                        "interval": "yearly"
                    })
                elif 25 <= avg_interval <= 35:
                    subscriptions.append({
                        "description": key[0],
                        "amount": key[1],
                        "interval": "monthly"
                    })
                elif 6 <= avg_interval <= 9:
                    subscriptions.append({
                        "description": key[0],
                        "amount": key[1],
                        "interval": "weekly"
                    })
        return subscriptions               



    elif timeframe > 1:
        #can allow for weekly and monthly subscriptions
        for transaction in transactions:
            if transaction.amount < 0:
                key = (transaction.description.lower(), round(transaction.amount,2))
                groups[key].append(transaction)
        subscriptions = []

        for key, recurring in groups.items():
            if len(recurring) > 2:
                recurring = sorted(recurring, key=lambda x: x.date)

                intervals = [
                    (recurring[i].date - recurring[i - 1].date).days
                    for i in range(1, len(recurring))
                ]

                avg_interval = sum(intervals) / len(intervals)
                if 6 <= avg_interval <= 9:
                    subscriptions.append({
                        "description": key[0],
                        "amount": key[1],
                        "interval": "weekly"
                    })
                elif 25 <= avg_interval <= 35:
                    subscriptions.append({
                        "description": key[0],
                        "amount": key[1],
                        "interval": "monthly"
                    })
                
        return subscriptions     

        
    else:
        return {"response": "Timeframe must be at least 1 month."}

