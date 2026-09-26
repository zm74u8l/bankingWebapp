# Banking Webapp

A small FastAPI + Streamlit app for poking at your own transaction history:
upload a CSV export, browse it, and ask it simple questions.

## Features

- Upload a CSV of transactions (stored via SQLAlchemy/SQLite)
- Browse accounts and transactions in a Streamlit UI
- A rule-based `/chat` endpoint that answers questions like total spend,
  highest transaction, and recurring subscriptions

## Stack

FastAPI · SQLAlchemy · Streamlit · SQLite

## Running it

```
pip install -r requirements.txt

# backend
uvicorn backend.main:app --reload

# frontend, in another shell
streamlit run frontend/app.py
```

The frontend expects the backend at `http://127.0.0.1:8000` by default —
set `API_URL` if you're running it elsewhere.
