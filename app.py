import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct"
headers = {"Authorization": f"Bearer YOUR_HF_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("🧠 FocusBuddy - Your Day Planner")

user_input = st.text_input("Say something to FocusBuddy 👇")

if st.button("Send") and user_input:
    output = query({"inputs": user_input})
    st.write("💬 FocusBuddy:", output[0]["generated_text"])
