import streamlit as st
import pandas as pd

# =========================
# Judul & Pengantar
# =========================
st.title("Sesi 2 — Layout & Komponen Teks")
st.subheader("Pengaturan Tampilan Dasar untuk Aplikasi Streamlit")

st.markdown("""
Modul ini menunjukkan bagaimana membuat tampilan yang rapi menggunakan beberapa elemen:
- Komponen teks (title, header, markdown)
- Sidebar
- Columns
- Container
- Expander
- Metric
""")

st.markdown("---")

# =========================
# Sidebar
# =========================
st.sidebar.header("Filter dan Input")

nama_pengguna = st.sidebar.text_input("Nama Pengguna")
kategori = st.sidebar.selectbox("Pilih Kategori", ["Kategori A", "Kategori B", "Kategori C"])
batas_usia = st.sidebar.slider("Rentang Usia", 10, 70, 30)

st.sidebar.write("Input tersimpan otomatis setelah perubahan.")


# =========================
# Bagian Statistik
# =========================
st.header("Statistik Utama")

col1, col2, col3 = st.columns(3)

col1.metric("Total Pelanggan", "12.530", "+120")
col2.metric("Pelanggan Baru", "320", "+12")
col3.metric("Retensi", "87%", "-2%")

st.markdown("---")

# =========================
# Penjelasan & Markdown
# =========================
st.subheader("Penjelasan Singkat")

st.markdown(f"""
Data berikut disesuaikan dengan pilihan kategori **{kategori}**  
dan rentang usia **{batas_usia} tahun**.

Nama pengguna yang dimasukkan:  
**{nama_pengguna if nama_pengguna else 'Belum ada'}**
""")

# =========================
# Dataframe Demo
# =========================
st.subheader("Contoh Dataframe")

df = pd.DataFrame({
    "Nama": ["Andi", "Budi", "Citra", "Dewi"],
    "Usia": [25, 30, 28, 35],
    "Kategori": ["Kategori A", "Kategori B", "Kategori A", "Kategori C"]
})

st.dataframe(df)

# =========================
# Expander
# =========================
with st.expander("Lihat Detail Tambahan"):
    st.write("""
    Bagian ini menampilkan informasi tambahan
    yang tidak perlu selalu terlihat. Expander bermanfaat
    untuk menyimpan catatan, dokumentasi, maupun data pendukung.
    """)

# =========================
# Container untuk Catatan
# =========================
catatan = st.container()
catatan.markdown("### Catatan Penting")
catatan.write("""
Perubahan pada input di sidebar akan memengaruhi hasil analisis.
Pastikan kategori dan rentang usia dipilih sesuai kebutuhan.
""")

# =========================
# Footer
# =========================
st.markdown("---")
st.caption("Sesi 2 — Layout & Komponen Teks | Streamlit Training")
