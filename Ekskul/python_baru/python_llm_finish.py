import streamlit as st
from openai import OpenAI
import base64
import PyPDF2
from io import BytesIO

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Hybrid Chatbot", page_icon="🧠", layout="wide")
st.title("🤖 Hybrid Chatbot (Llama 3.3 + Vision + Qwen Backup)")

# --- KONFIGURASI MODEL (Ubah di sini jika ada update dari Groq) ---
MODEL_VISION = "llama-3.2-11b-vision-preview"  # Ganti ke 11b karena 90b sudah decommissioned
MODEL_TEXT_MAIN = "llama-3.3-70b-versatile"
MODEL_TEXT_BACKUP = "qwen-2.5-32b"

# Setup Client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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" 
)

# --- FUNGSI BANTUAN ---
def encode_image(uploaded_file):
    return base64.b64encode(uploaded_file.getvalue()).decode('utf-8')

def extract_text_from_pdf(uploaded_file):
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error membaca PDF: {e}"

def generate_answer(history, model_list):
    system_prompt = {
        "role": "system", 
        "content": (
            "You are an expert AI assistant. "
            "For coding questions, provide clean, efficient, and commented code. "
            "For document analysis, be precise and cite the text provided. "
            "If the user speaks Indonesian, reply in Indonesian."
        )
    }
    
    messages_to_send = [system_prompt] + history
    last_error = None
    
    for model_id in model_list:
        try:
            # Model vision butuh token output lebih sedikit untuk menghindari timeout
            max_tok = 1024 if "vision" in model_id else 2048
            
            response = client.chat.completions.create(
                model=model_id,
                messages=messages_to_send,
                temperature=0.6,
                max_tokens=max_tok
            )
            return response.choices[0].message.content, model_id
            
        except Exception as e:
            last_error = e
            print(f"Model {model_id} gagal: {e}. Mencoba backup...")
            continue 
            
    return f"Maaf, semua model sedang sibuk atau error. Detail: {last_error}", "Error"

# --- 2. SESSION STATE ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {"Chat 1": []}
if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = "Chat 1"

# --- 3. SIDEBAR ---
st.sidebar.title("🗂️ Chat History")
if st.sidebar.button("➕ New Chat"):
    new_id = f"Chat {len(st.session_state.chat_history) + 1}"
    st.session_state.chat_history[new_id] = []
    st.session_state.current_chat_id = new_id

for chat_id in st.session_state.chat_history:
    if st.sidebar.button(chat_id):
        st.session_state.current_chat_id = chat_id

# --- 4. MAIN AREA ---
active_id = st.session_state.current_chat_id
st.header(f"💬 {active_id}")

for msg in st.session_state.chat_history[active_id]:
    with st.chat_message(msg["role"]):
        if "display_file" in msg:
            st.info(f"📎 File: {msg['display_file']}")
        if "used_model" in msg:
            st.caption(f"⚡ Dijawab oleh: {msg['used_model']}")

        if isinstance(msg["content"], list):
            for part in msg["content"]:
                if part["type"] == "text":
                    st.write(part["text"])
                elif part["type"] == "image_url":
                    if "display_image" in msg:
                        st.image(msg["display_image"], width=300)
        else:
            st.write(msg["content"])

# --- 5. INPUT AREA ---
with st.container():
    col1, col2 = st.columns([0.1, 0.9]) 
    with col1:
        with st.popover("📎", use_container_width=True):
            st.write("Upload:")
            uploaded_file = st.file_uploader("", type=["jpg", "png", "pdf", "txt", "csv", "py"], key="uploader")

if prompt := st.chat_input("Ketik pesan..."):
    
    models_to_try = []
    
    if uploaded_file:
        file_type = uploaded_file.type
        
        # KASUS 1: GAMBAR -> Wajib Vision Model
        if "image" in file_type:
            base64_image = encode_image(uploaded_file)
            api_content = [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
            memory_content = api_content
            extra_metadata = {"display_image": uploaded_file}
            
            # --- PERBAIKAN DI SINI ---
            models_to_try = [MODEL_VISION] 
            
        # KASUS 2: DOKUMEN -> Text Model
        else:
            if "pdf" in file_type:
                extracted_text = extract_text_from_pdf(uploaded_file)
            else:
                stringio = BytesIO(uploaded_file.getvalue())
                extracted_text = stringio.read().decode("utf-8")
            
            full_prompt = f"User uploaded content:\n\n{extracted_text}\n\nUser Question: {prompt}"
            api_content = full_prompt
            memory_content = prompt 
            extra_metadata = {"display_file": uploaded_file.name}
            
            models_to_try = [MODEL_TEXT_MAIN, MODEL_TEXT_BACKUP]
            
    else:
        # KASUS 3: CHAT BIASA
        api_content = prompt
        memory_content = prompt
        extra_metadata = {}
        
        models_to_try = [MODEL_TEXT_MAIN, MODEL_TEXT_BACKUP]

    # --- SIMPAN & PROSES ---
    user_msg_obj = {
        "role": "user",
        "content": memory_content,
        "api_payload": api_content
    }
    user_msg_obj.update(extra_metadata)
    st.session_state.chat_history[active_id].append(user_msg_obj)
    
    with st.chat_message("user"):
        if "display_file" in extra_metadata:
            st.info(f"📎 {extra_metadata['display_file']}")
        if "display_image" in extra_metadata:
            st.image(extra_metadata['display_image'], width=300)
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner(f"Mencoba model terbaik: {models_to_try[0]}..."):
            clean_history = []
            for m in st.session_state.chat_history[active_id]:
                if isinstance(m.get("api_payload"), list) and "vision" not in models_to_try[0]:
                     clean_history.append({"role": m["role"], "content": "[User sent an image]"})
                else:
                     content_to_send = m.get("api_payload", m["content"])
                     clean_history.append({"role": m["role"], "content": content_to_send})
            
            answer, used_model = generate_answer(clean_history, models_to_try)
            st.write(answer)
            st.caption(f"⚡ Model: {used_model}")
    
    st.session_state.chat_history[active_id].append({
        "role": "assistant", 
        "content": answer,
        "used_model": used_model
    })