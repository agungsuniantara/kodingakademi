import streamlit as st

st.title("Counter App (Buggy)")

count = 0 

if st.button("Plus"):
    count += 1

st.write("Count:", count)

st.title("Counter App (Fixed)")

# 1. Initialization: Check if 'count' exists in session_state
if 'count' not in st.session_state:
    st.session_state['count'] = 0

# 2. Interaction: Update the value in session_state
if st.button("Increment"):
    st.session_state['count'] += 1

st.write("Current Count:", st.session_state['count'])

st.title("Simple Chat UI")

# Display a user message
with st.chat_message("user"):
    st.write("Hello, how are you?")

# Display an assistant message
with st.chat_message("assistant"):
    st.write("I am fine, thank you! How can I help?")

# Chat Input (Visual only, no logic yet)
prompt = st.chat_input("Say something...")
if prompt:
    st.write(f"User sent: {prompt}")