import streamlit as st

# 1. Initialize the storage for ALL chats
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {
        "Chat 1": [] # Start with one empty chat
    }

# 2. Initialize the tracker for the CURRENT active chat
if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = "Chat 1"
    
# Sidebar Title
st.sidebar.title("Chat History")

# --- 'New Chat' Button Logic ---
if st.sidebar.button("➕ New Chat"):
    # Generate a new ID based on the number of existing chats
    new_id = f"Chat {len(st.session_state.chat_history) + 1}"
    
    # Create an empty list for this new chat
    st.session_state.chat_history[new_id] = []
    
    # Switch focus to the new chat
    st.session_state.current_chat_id = new_id

# --- Display Existing Chat Buttons ---
st.sidebar.write("---") # Divider
# Loop through all available chat IDs
for chat_id in st.session_state.chat_history:
    # If a button is clicked, update the current active chat
    if st.sidebar.button(chat_id):
        st.session_state.current_chat_id = chat_id

# Display the name of the current chat
active_id = st.session_state.current_chat_id
st.title(f"{active_id}")

# 1. Load History for the Active ID
current_messages = st.session_state.chat_history[active_id]

# 2. Display Messages
for message in current_messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 3. Handle New Input
if prompt := st.chat_input("Type a message..."):
    # Show User Message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Save to History
    st.session_state.chat_history[active_id].append({"role": "user", "content": prompt})

    # Simulate Bot Response (Echo)
    response = prompt
    with st.chat_message("assistant"):
        st.write(response)
    
    # Save Bot Response to History
    st.session_state.chat_history[active_id].append({"role": "assistant", "content": response})