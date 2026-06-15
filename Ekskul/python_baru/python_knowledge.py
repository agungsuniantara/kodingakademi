import streamlit as st

KNOWLEDGE_BASE = {
    "hello": "Hi! I am your Python Knowledge Assistant.",
    "what is python": "Python is a popular, high-level programming language.",
    "what is streamlit": "Streamlit is a Python library for building web apps.",
    "how to run": "Use the command: streamlit run app.py",
    "bye": "Goodbye! Happy coding."
}

def get_answer(query):
    clean_query = query.lower()
    
    for key in KNOWLEDGE_BASE:
        if key in clean_query:
            return KNOWLEDGE_BASE[key]
            
    return "I do not understand."

if "chat_history" not in st.session_state:
    st.session_state.chat_history = {
        "Chat 1": [] 
    }

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = "Chat 1"
    
st.sidebar.title("Chat History")

if st.sidebar.button("➕ New Chat"):
    new_id = f"Chat {len(st.session_state.chat_history) + 1}"

    st.session_state.chat_history[new_id] = []

    st.session_state.current_chat_id = new_id

st.sidebar.write("---")
for chat_id in st.session_state.chat_history:
    if st.sidebar.button(chat_id):
        st.session_state.current_chat_id = chat_id

active_id = st.session_state.current_chat_id
st.title(f"{active_id}")

current_messages = st.session_state.chat_history[active_id]

for message in current_messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Type a message..."):
    with st.chat_message("user"):
        st.write(prompt)
    
    st.session_state.chat_history[active_id].append({"role": "user", "content": prompt})

    response = get_answer(prompt)
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.chat_history[active_id].append({"role": "assistant", "content": response})
