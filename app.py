import streamlit as st
import requests

# ✅ Use your actual Hugging Face token here
HF_TOKEN = "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"

# ✅ Set DeepSeek model URL
API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-V3-0324"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("🧠 FocusBuddy - Your Day Planner")

user_input = st.text_input("Say something to FocusBuddy 👇")

if st.button("Send") and user_input:
    with st.spinner("Thinking..."):
        output = query({"inputs": user_input})
        try:
            st.write("💬 FocusBuddy:", output[0]["generated_text"])
        except (KeyError, IndexError, TypeError):
            st.warning("⚠️ The model didn’t return any response. Try again after a few seconds.")
            st.json(output)
