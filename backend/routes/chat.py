from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.services.analytics import total_spend, max_transaction, subscriptions
from backend.database import get_db
import re

router = APIRouter(prefix="/chat")

@router.post("/")
def chat(prompt:str, db: Session = Depends(get_db)):
    print(prompt)
    if "total" in prompt.lower() or "spend" in prompt.lower():
        spendings = total_spend(db)
        total = abs(sum([amount for (amount,) in spendings]))
        return {"response": f"Your total spendings are: {total:.2f}"}
    elif "max" in prompt.lower() or "highest" in prompt.lower():
        max = max_transaction(db)
        return {"response": f"Your highest transaction is: {max.amount:.2f}, on {max.date}, at {max.description}"}
    elif "subscriptions" in prompt.lower():
        if re.search("[0-9]+", prompt.lower()):
            subs = subscriptions(int(re.search("[0-9]+", prompt.lower()).group()), db)
        else:
            subs = subscriptions(48, db)

        if len(subs) == 0:
            return {"response": f"You have no subscriptions"}
        elif len(subs)<2:
            return {"response": f"You have a/an {subs[0]["description"]} subscription, which costs {abs(subs[0]["amount"]):.2f} on a {subs[0]["interval"]} interval"}
        else:
            built_string = ""
            for i in range(len(subs)):
                if i == (len(subs)-1):
                    built_string = built_string + f"and finally you have a/an {subs[i]["description"]} subscription, which costs {abs(subs[i]["amount"]):.2f} on a {subs[i]["interval"]} interval. "
                elif i == 0:
                    built_string = built_string + f"You have a/an {subs[i]["description"]} subscription, which costs {abs(subs[i]["amount"]):.2f} on a {subs[i]["interval"]} interval. "
                else:
                    built_string = built_string + f"You also have a/an {subs[i]["description"]} subscription, which costs {abs(subs[i]["amount"]):.2f} on a {subs[i]["interval"]} interval."
            return {"response": built_string}    

        
    return {"response": "I'm sorry, I couldn't help you."}