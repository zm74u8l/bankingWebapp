import streamlit as st 
import requests
import os
import pandas as pd
from dotenv import load_dotenv


load_dotenv()
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("Welcome to the Banking App Frontend")
st.write("This is a simple frontend interface for My Banking App backend.")

st.header("Accounts")
accounts = requests.get(f"{API_URL}/accounts/").json()
st.dataframe(pd.DataFrame(accounts))

st.header("Transactions")
transactions = requests.get(f"{API_URL}/transactions/").json()
st.dataframe(pd.DataFrame(transactions))

