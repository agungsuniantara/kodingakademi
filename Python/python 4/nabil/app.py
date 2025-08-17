import streamlit as st
import pandas as pd

st.title("Contoh test Streamlit")

uploaded_file = st.file_uploader("Upload file CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)  # Tampilkan tabel data