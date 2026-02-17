import streamlit as st 
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("Welcome to the Banking App Frontend")
st.write("This is a simple frontend interface for My Banking App backend.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("Ask about your spending...")
if prompt:
    st.chat_message("user").write(prompt)
    res = requests.post(f"{API_URL}/chat/", params={"prompt": prompt}).json()

    st.chat_message("assistant").write(res["response"])
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": res["response"]})