from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat(history=[])

def get_gimini_response(question):
    response = chat.send_message(question, stream=True)
    
    return response

st.set_page_config(page_title="Simple Q/A ChatBot")
st.title("Simple Q/A ChatBot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:", key="input")

submit = st.button("Ask the question")

if submit and input:
    response = get_gimini_response(input)
    
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

