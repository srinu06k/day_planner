import streamlit as st
import requests

# 🔐 Replace with your Hugging Face token
HF_TOKEN = "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"
# 🔁 Replace with your chosen DeepSeek model
API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-llm-7b-chat"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {
            "error": "Invalid JSON response",
            "status_code": response.status_code,
            "text": response.text
        }

# Streamlit UI
st.title("🧠 FocusBuddy - Powered by DeepSeek")

user_input = st.text_input("💬 Say something to FocusBuddy:")

if st.button("Send") and user_input:
    with st.spinner("🤖 Thinking..."):
        # For chat-style models like DeepSeek
        payload = {
            "inputs": {
                "past_user_inputs": [],
                "generated_responses": [],
                "text": user_input
            }
        }

        output = query(payload)

        if "error" in output:
            st.error(f"❌ API Error: {output['error']}")
            st.code(output.get("text", ""), language="text")
        else:
            try:
                response_text = output["generated_text"] if "generated_text" in output[0] else output[0]["generated_text"]
                st.success("💬 FocusBuddy:")
                st.write(response_text)
            except (KeyError, IndexError, TypeError):
                st.warning("⚠️ The model didn’t return a valid response.")
                st.json(output)























