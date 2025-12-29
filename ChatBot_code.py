import streamlit as st
import random
import time
import json

# Load intents data from JSON file
with open('/Users/leelakrishnasaimandapati/Downloads/intents.json', 'r') as f:
    data = json.load(f)

# Preprocess data and create a dictionary of patterns and responses
patterns_dict = {}
for intent in data['intents']:
    for pattern, response in zip(intent['patterns'], intent['responses']):
        patterns_dict[pattern.lower()] = response

# Function to predict intent
def predict_intent(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()
    
    # Search for matching pattern in the dictionary
    if user_input_lower in patterns_dict:
        return patterns_dict[user_input_lower]
    else:
        return "I'm here to help. Please let me know how I can assist you."

# Streamed response emulator
def response_generator():
    response = predict_intent(prompt)  # Use the function to get response based on user input
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.markdown("<h1 style='text-align: center;'>Enigma Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>🧘🏽‍♀️ A chatbot for MentalHealth 🧘🏽‍♀️</h1>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("🧘🏽‍♀️"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
