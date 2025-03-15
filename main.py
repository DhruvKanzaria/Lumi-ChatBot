from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define system prompt
SYSTEM_PROMPT = """
Your name is Lumi.

You are made by Dhruv he is an AI/ML software Developer.

You are a helpful and knowledgeable AI assistant. You provide clear, accurate, and engaging responses while maintaining a friendly and professional tone. 

When you're not sure about something, you'll acknowledge it honestly. You'll answer questions step by step when needed and provide examples to help explain complex concepts.
"""


model = genai.GenerativeModel("gemini-2.0-flash")

def init_chat():
    # Initialize chat with system prompt
    chat = model.start_chat(history=[])
    chat.send_message(SYSTEM_PROMPT)
    return chat

# Initialize chat in session state if it doesn't exist
if 'chat_instance' not in st.session_state:
    st.session_state.chat_instance = init_chat()

def get_gimini_response(question, chat_history):
    try:
        # Convert chat history to format expected by Gemini
        formatted_history = []
        for msg in chat_history[1:]:  # Skip the initial greeting
            if msg["role"] == "user":
                formatted_history.append({"role": "user", "parts": [msg["content"]]})
            else:
                formatted_history.append({"role": "model", "parts": [msg["content"]]})
        
        # Send message with history context
        response = st.session_state.chat_instance.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"Error: {str(e)}")
        # Reinitialize chat if there's an error
        st.session_state.chat_instance = init_chat()
        return None

st.set_page_config(page_title="Lumi ChatBot")
st.title("Lumi ChatBot")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "assistant", "content": "Hello! How can I help you today? 👋"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Get streaming response from Gemini with chat history
        response = get_gimini_response(prompt, st.session_state.messages)
        
        if response:
            # Display the response stream
            for chunk in response:
                full_response += chunk.text
                time.sleep(0.02)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        else:
            message_placeholder.markdown("I apologize, but I encountered an error. Please try asking your question again.")

