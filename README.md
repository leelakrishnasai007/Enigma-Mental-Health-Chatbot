# Enigma Chatbot (Mental Health Support) – Streamlit + Python

A simple, intent-based mental health support chatbot built with Python and Streamlit.  
It uses a structured dataset of patterns and responses (intents.json) to identify what the user is trying to express (intent) and reply with a supportive response.

This project is designed as a clean, beginner-friendly example of:
- building a chatbot UI using Streamlit
- using an intent-based dataset (patterns + responses)
- deploying a small working AI-style application with a clear structure

------------------------------------------------------------

Why this project?

Mental health support is often hard to access quickly, and many people also feel uncomfortable asking for help.
This project demonstrates how a chatbot can:
- provide a safe starting point for conversation
- respond with empathetic messages
- guide users toward helpful next steps

Important note: This is not a replacement for professional care. It is an educational/demo project.

------------------------------------------------------------

What the project does (high-level)

Think of this project as a small pipeline:

1) User types a message in the Streamlit chat UI  
2) The app loads the dataset (intents.json)  
3) It detects the intent by comparing the user message to patterns  
4) It selects a relevant response for that intent  
5) The response is shown back in the chat UI

This creates a therapist-style supportive conversation experience using a structured dataset.

------------------------------------------------------------

System Overview (architecture)

Streamlit UI (chat interface)
        |
        v
Intent Matcher (pattern lookup / matching)
        |
        v
Response Selector (choose a response for the detected intent)
        |
        v
Chat Output (display response + save chat history in session)

Key idea:
- The dataset is the brain of the chatbot.
- The Streamlit app is the face of the chatbot.

------------------------------------------------------------

Features

1) Streamlit chat interface
- Clean chat experience similar to modern chat apps
- Chat history stays during the session

2) Intent-based conversation handling
- Recognizes user intent using dataset patterns
- Example intents: greeting, sad, stressed, anxious, depressed, etc.

3) Structured dataset usage (intents.json)
- Easy to edit
- Easy to expand (add new intents, patterns, responses)

4) Beginner-friendly and readable logic
- The logic is kept simple so anyone can understand how it works

------------------------------------------------------------

About Dataset (intents.json)

This project uses an existing mental health conversational dataset containing:
- basic conversations
- mental health FAQ
- therapy-style conversations
- general advice for anxiety and depression support

The dataset contains intents.

What is an intent?
An intent is the intention behind a user message.
Example:
If the user says “I am sad”, the intent could be “sad”.

Each intent contains:
- tag: the name of the intent
- patterns: example user inputs that represent this intent
- responses: chatbot replies for that intent

This structure allows the chatbot to behave in a therapist-like supportive manner using predefined responses.

------------------------------------------------------------

How to Run (local)

1) Clone the repository
git clone <your-repo-url>
cd enigma-mental-health-chatbot

2) Install dependencies
pip install -r requirements.txt

3) Run Streamlit
streamlit run ChatBot.py

(If your main file is app.py)
streamlit run app.py

------------------------------------------------------------

How to Use

1) Start the Streamlit app
2) Type a message like:
- Hi
- I feel sad
- I am stressed
- I feel anxious
3) The chatbot replies based on the closest matching intent patterns
4) Continue the conversation as needed

------------------------------------------------------------

Limitations

This chatbot is intent-based and uses pattern matching from the dataset.
That means:
- It works best when the user message is close to the patterns
- It may not understand completely new wording
- It does not generate new responses like large language models (LLMs)

These limitations are normal for a beginner-friendly chatbot and are part of why this project is easy to understand and improve.

------------------------------------------------------------

Future Improvements (good for interviews)

If you want to upgrade this project later, strong improvements are:

1) Better intent detection
- use text similarity (TF-IDF / cosine similarity)
- or train a small classifier model (SVM / Logistic Regression)

2) Smarter response selection
- pick randomly from responses for variety
- add context memory across turns

3) Safety improvements
- detect crisis-related intent and show proper help resources
- add stronger disclaimers and escalation steps

4) Upgrade to an LLM-based chatbot (optional)
- use RAG (Retrieval-Augmented Generation)
- store intents and therapy knowledge in a vector database
- keep Streamlit UI as frontend