import streamlit as st
from openai import OpenAI

# --- 1. CONFIGURATION ---
st.title("Smart Chatbot (Groq Edition) 🚀")

# Configure Client to point to Groq's Cloud Server
# REPLACE 'gsk_...' WITH YOUR ACTUAL API KEY
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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" 
)

# --- 2. KNOWLEDGE BASE (The Facts) ---
knowledge_db = {
    "python": "Python is a high-level, interpreted programming language known for readability.",
    "streamlit": "Streamlit is an open-source framework used to build data web apps in pure Python.",
    "variable": "A variable is a symbolic name associated with a value and whose associated value may be changed.",
    "loop": "A loop is a sequence of instruction that is continually repeated until a certain condition is reached."
}

# --- 3. RETRIEVAL FUNCTION ---
# (This logic remains the same as the Knowledge Base module)
def retrieve_context(query):
    query = query.lower()
    # for key, value in knowledge_db.items():
    #     if key in query:
    #         return value
    return query

# --- 4. GENERATION FUNCTION ---
def generate_answer(query, context):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", # We use Llama 3 (very smart & fast)
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are a helpful assistant."
                    )
                },
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Groq: {e}"

# --- 5. SESSION STATE & UI ---
# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {"Chat 1": []}
if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = "Chat 1"

# Sidebar for History
st.sidebar.title("Chat History")
if st.sidebar.button("➕ New Chat"):
    new_id = f"Chat {len(st.session_state.chat_history) + 1}"
    st.session_state.chat_history[new_id] = []
    st.session_state.current_chat_id = new_id

for chat_id in st.session_state.chat_history:
    if st.sidebar.button(chat_id):
        st.session_state.current_chat_id = chat_id

# Main Chat Interface
active_id = st.session_state.current_chat_id
st.header(f"💬 {active_id}")

# Display History
for msg in st.session_state.chat_history[active_id]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input Handling
if prompt := st.chat_input("Ask about Python concepts..."):
    # 1. User Message
    st.session_state.chat_history[active_id].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 2. Retrieval & Generation
    context = retrieve_context(prompt)
    if context:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = generate_answer(prompt, context)
                st.write(answer)
        st.session_state.chat_history[active_id].append({"role": "assistant", "content": answer})
    else:
        fallback = "I don't have information about that in my database."
        with st.chat_message("assistant"):
            st.write(fallback)
        st.session_state.chat_history[active_id].append({"role": "assistant", "content": fallback})