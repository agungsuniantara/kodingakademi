import streamlit as st
from openai import OpenAI
import PyPDF2
from io import BytesIO

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Coding Assistant", page_icon="💻", layout="wide")
st.title("💻 Pro Coding Assistant (Qwen 3 + Llama 3.3)")

# --- KONFIGURASI MODEL BERDASARKAN DATA ANDA ---
# Kita gunakan Qwen 3 sebagai UTAMA karena Anda fokus coding & materi
MODEL_MAIN = "qwen/qwen3-32b" 
MODEL_BACKUP = "llama-3.3-70b-versatile"

# Setup Client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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" 
)

# --- FUNGSI BANTUAN ---
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
    """
    Sistem Auto-Switch: Coba Qwen 3 -> Jika gagal -> Coba Llama 3.3
    """
    system_prompt = {
        "role": "system", 
        "content": (
            "You are an expert Senior Software Engineer and Educator. "
            "When asked to code, provide efficient, secure, and modern solutions. "
            "Explain concepts clearly like a teacher. "
            "If user asks in Indonesian, answer in Indonesian."
        )
    }
    
    messages_to_send = [system_prompt] + history
    last_error = None
    
    for model_id in model_list:
        try:
            response = client.chat.completions.create(
                model=model_id,
                messages=messages_to_send,
                temperature=0.5, # Balance antara kreatif dan presisi
                max_tokens=2048
            )
            return response.choices[0].message.content, model_id
            
        except Exception as e:
            last_error = e
            print(f"Model {model_id} gagal. Mencoba backup...")
            continue 
            
    return f"Maaf, server sedang sibuk. Error: {last_error}", "Error"

# --- 2. SESSION STATE ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {"Chat 1": []}
if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = "Chat 1"

# --- 3. SIDEBAR ---
st.sidebar.title("🗂️ Project History")
if st.sidebar.button("➕ New Project"):
    new_id = f"Project {len(st.session_state.chat_history) + 1}"
    st.session_state.chat_history[new_id] = []
    st.session_state.current_chat_id = new_id

for chat_id in st.session_state.chat_history:
    if st.sidebar.button(chat_id):
        st.session_state.current_chat_id = chat_id

# --- 4. MAIN AREA ---
active_id = st.session_state.current_chat_id
st.header(f"🚀 {active_id}")

for msg in st.session_state.chat_history[active_id]:
    with st.chat_message(msg["role"]):
        if "display_file" in msg:
            st.info(f"📄 File Context: {msg['display_file']}")
        
        # Tampilkan teks biasa
        st.write(msg["content"])
        
        if "used_model" in msg:
            st.caption(f"⚡ {msg['used_model']}")

# --- 5. INPUT AREA ---
# Kita hapus Image Uploader karena tidak ada model vision yang tersedia
with st.container():
    col1, col2 = st.columns([0.1, 0.9]) 
    with col1:
        with st.popover("📎", use_container_width=True):
            st.write("Upload Code/Doc:")
            # Fokus pada file teks/coding
            uploaded_file = st.file_uploader("", type=["pdf", "txt", "csv", "py", "js", "html"], key="uploader")

if prompt := st.chat_input("Tanya soal coding atau upload file..."):
    
    # Siapkan container pesan
    api_content = prompt
    memory_content = prompt
    extra_metadata = {}
    
    # Logika Upload File (Text Extractor)
    if uploaded_file:
        file_type = uploaded_file.type
        file_name = uploaded_file.name
        
        # Ekstrak konten berdasarkan tipe
        if "pdf" in file_type:
            extracted_text = extract_text_from_pdf(uploaded_file)
        else:
            # Untuk script coding (py, js, html, txt)
            stringio = BytesIO(uploaded_file.getvalue())
            extracted_text = stringio.read().decode("utf-8")
        
        # Gabungkan ke prompt
        api_content = f"User uploaded file '{file_name}':\n\n```\n{extracted_text}\n```\n\nQuestion: {prompt}"
        extra_metadata = {"display_file": file_name}
    
    # Simpan Input User
    user_msg_obj = {
        "role": "user",
        "content": memory_content,
        "api_payload": api_content
    }
    user_msg_obj.update(extra_metadata)
    st.session_state.chat_history[active_id].append(user_msg_obj)
    
    with st.chat_message("user"):
        if "display_file" in extra_metadata:
            st.info(f"📄 {extra_metadata['display_file']}")
        st.write(prompt)

    # Generate Jawaban
    with st.chat_message("assistant"):
        # Prioritas: Qwen 3 (Coding) -> Llama 3.3 (Logic Backup)
        models_to_try = [MODEL_MAIN, MODEL_BACKUP]
        
        with st.spinner(f"Coding dengan {models_to_try[0]}..."):
            clean_history = []
            for m in st.session_state.chat_history[active_id]:
                content = m.get("api_payload", m["content"])
                clean_history.append({"role": m["role"], "content": content})
            
            answer, used_model = generate_answer(clean_history, models_to_try)
            
            st.write(answer)
            # Indikator warna hijau jika pakai Qwen (Main), kuning jika Backup
            if used_model == MODEL_MAIN:
                st.caption(f"⚡ Powered by: {used_model} (Primary)")
            else:
                st.caption(f"⚠️ Powered by: {used_model} (Backup)")
    
    st.session_state.chat_history[active_id].append({
        "role": "assistant", 
        "content": answer,
        "used_model": used_model
    })