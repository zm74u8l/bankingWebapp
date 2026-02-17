import streamlit as st 
import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("Welcome to the Banking App Frontend")
st.write("This is a simple frontend interface for My Banking App backend.")

st.header("Upload CSV")
uploaded_csv = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_csv is not None:
    files = 0
    response = requests.post(f"{API_URL}/transactions/upload-csv", files={"file": uploaded_csv})

    if response.status_code == 200:
        st.success({"message": response.json()["message"]})
        st.switch_page("app.py")

    if response.status_code != 200:
        st.error("Failed to upload CSV file.")
