import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.title("Sherketna 🤖")

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

question = st.text_input("Ask Sherketna AI:")

if question:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    st.write(response.text)