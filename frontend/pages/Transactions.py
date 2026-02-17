import streamlit as st
import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("Welcome to the Banking App Frontend")
st.write("This is a simple frontend interface for My Banking App backend.")

st.header("Filter your Transactions")

transactions = requests.get(f"{API_URL}/transactions/").json()
dataframe = pd.DataFrame(transactions)

st.dataframe(dataframe, width="stretch")

st.subheader("filters")

sorted_dataframe= sorted(dataframe["category"].dropna().unique())

for i in sorted_dataframe:
    if not i.strip():
        sorted_dataframe[i] = "Undefined"

categories = ["All"] + sorted_dataframe
chosen_category = st.selectbox("Categories", categories)

