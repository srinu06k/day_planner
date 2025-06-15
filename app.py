import streamlit as st
import requests

# ✅ Replace with your actual Hugging Face token
HF_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("🧠 FocusBuddy - Your Day Planner")

user_input = st.text_input("Say something to FocusBuddy 👇")

if st.button("Send") and user_input:
    output = query({"inputs": user_input})
    
    # ✅ Moved try block inside the condition to avoid undefined 'output'
  if st.button("Send") and user_input:
    output = query({"inputs": user_input})
    try:
        st.write("💬 FocusBuddy:", output[0]["generated_text"])
    except (KeyError, IndexError, TypeError):
        st.warning("⚠️ The model didn’t return any response. Try again after a few seconds.")
        st.json(output)  # Optional: View raw output

