import streamlit as st
import requests
import os
import google.generativeai as genai


def get_api_key():
    # Securely fetch the API key from environment variables
    return os.getenv("CHATBOT_API_KEY")

st.title("Chatbot Application")

user_input = st.text_input("You: ", "Hello, how are you?")

if st.button("Send"):
    api_key = "AIzaSyDhDNoRF6Iv1h3Xo4Xy-nMDgegQ9Tn3Vv8"
    if not api_key:
        st.error("Error: API key not found. Please set the CHATBOT_API_KEY environment variable.")
    else:
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel('gemini-1.5-flash')
        
        try:
            bot_response = model.generate_content(user_input).text

            if bot_response:
                st.text_area("Bot:", bot_response, height=200)
            else:
                st.error("Error: No response from the bot.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")