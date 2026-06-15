import streamlit as st
import requests
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="InsightAI: Data Scientist", layout="wide")

st.title("🤖 InsightAI: Automated Data Scientist")

# --- SIDEBAR (Upload File) ---
with st.sidebar:
    st.header("📂 Data Source")
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Baca CSV sekali dan simpan di session state agar performa cepat
            if "df" not in st.session_state or st.session_state.get("file_name") != uploaded_file.name:
                st.session_state.df = pd.read_csv(uploaded_file)
                st.session_state.file_name = uploaded_file.name
            
            st.success("File Berhasil di-load!")
            
            # --- TAMPILAN DATA (FULL) ---
            df = st.session_state.df
            
            st.write("---")
            st.write(f"**Total Data:** {len(df)} baris")
            
            # Tampilkan SEMUA data langsung
            # height=600 agar tabel cukup tinggi dan enak di-scroll
            st.dataframe(df, height=600) 
            st.caption("ℹ️ Tabel menampilkan seluruh data. Gunakan scroll untuk melihat ke bawah.")
            
        except Exception as e:
            st.error(f"Gagal membaca CSV: {e}")

# --- MAIN CHAT AREA ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render ulang history chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input User
if prompt := st.chat_input("Perintahkan AI Data Scientist Anda..."):
    if not uploaded_file:
        st.warning("⚠️ Mohon upload file CSV terlebih dahulu.")
    else:
        # 1. Tampilkan pesan user
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. Kirim ke Backend
        with st.chat_message("assistant"):
            with st.spinner("🤖 Sedang coding & training model..."):
                try:
                    uploaded_file.seek(0)
                    files = {'file': (uploaded_file.name, uploaded_file, 'text/csv')}
                    data = {'query': prompt}

                    api_url = "http://localhost:8000/analyze"
                    response = requests.post(api_url, files=files, data=data)

                    if response.status_code == 200:
                        json_res = response.json()
                        answer = json_res.get("answer", "Tidak ada jawaban.")
                        st.markdown(answer)
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                    else:
                        st.error(f"Server Error: {response.status_code}")

                except Exception as e:
                    st.error(f"Gagal terhubung ke Backend: {e}")