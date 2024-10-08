from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question) -> str:
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="ChatBot")
st.header("ChatBot")
input = st.text_input("Input :",key = "input")
submit = st.button("Ask the Question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)