import os
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

def get_agent_response(csv_path: str, query: str) -> str:
    try:
        # 1. Validasi API Key
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "Error: GOOGLE_API_KEY tidak ditemukan."

        # 2. Load Data
        df = pd.read_csv(csv_path, low_memory=False)

        # 3. Setup LLM (Gunakan versi stabil 1.5-flash)
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            temperature=0,
            google_api_key=api_key
        )

        # 4. PROMPT ENGINEERING (ANTI-LOOPING EXTREME)
        PREFIX = """
        Kamu adalah Data Scientist Python. Variabel 'df' SUDAH ADA.
        
        TUGAS:
        Jalankan kode Python untuk menjawab pertanyaan user.
        
        PANDUAN CODING (WAJIB DIPATUHI):
        1. IMPORTS: Selalu import library yang dibutuhkan di awal code block (misal: sklearn, seaborn, matplotlib).
        2. PREPROCESSING:
           - Sebelum modeling, cek missing values. Jika ada, lakukan imputasi (mean/median/mode).
           - Encode variabel kategori (OneHotEncoder atau LabelEncoder) jika diperlukan untuk model.
        3. MODELING:
           - Jika diminta prediksi angka (Regresi): Gunakan LinearRegression atau RandomForestRegressor.
           - Jika diminta prediksi kategori (Klasifikasi): Gunakan LogisticRegression atau RandomForestClassifier.
           - Jika diminta grouping (Clustering): Gunakan KMeans.
        4. EVALUASI:
           - Selalu split data menjadi Train/Test set (train_test_split).
           - Tampilkan metrik evaluasi (R2 Score, MSE, Accuracy, Confusion Matrix).
        5. VISUALISASI:
           - Jika membuat plot, gunakan matplotlib/seaborn.
           - Jangan gunakan plt.show(), tapi jelaskan insight dari plot tersebut.
        
        ATURAN KRUSIAL (BACA DENGAN TELITI):
        1. SETELAH KAMU MELIHAT HASIL 'Observation' DARI PYTHON, JANGAN MENULIS 'Action' LAGI.
        2. LANGSUNG TULIS: "Final Answer: [Jawaban Kamu]"
        3. JANGAN melakukan verifikasi ulang. Percayalah pada hasil eksekusi pertama.
        4. JANGAN membuat data dummy.
        
        CONTOH ALUR YANG BENAR (WAJIB DITIRU):
        Thought: Saya harus menjumlahkan kolom A.
        Action: python_repl_ast
        Action Input: print(df['A'].sum())
        Observation: 500
        Final Answer: Totalnya adalah 500.  <-- BERHENTI DI SINI
        
        JIKA KAMU MENGULANG-ULANG PROSES, KAMU AKAN DIMATIKAN.
        """

        # Fungsi penanganan error kustom
        # Jika Gemini 'ngelantur' (salah format), fungsi ini memaksa dia untuk memberikan jawaban akhir.
        def _handle_error(error) -> str:
            return str(error)[:50] + " ... (Error). Coba langsung berikan Final Answer dari hasil yang sudah kamu lihat sebelumnya."

        # 5. Buat Agent
        agent = create_pandas_dataframe_agent(
            llm,
            df,
            verbose=True,
            allow_dangerous_code=True,
            prefix=PREFIX,
            agent_executor_kwargs={
                "handle_parsing_errors": _handle_error # Gunakan handler kustom
            },
            max_iterations=5, # Batas loop
            include_df_in_prompt=True
        )

        # 6. Eksekusi
        response = agent.invoke(query)
        return response['output']

    except Exception as e:
        # Fallback jika benar-benar macet
        if "iteration limit" in str(e).lower():
            return "Analisis selesai. Jawaban kemungkinan sudah ditemukan di langkah sebelumnya (Cek Terminal), tapi Agent lupa menuliskannya."
        return f"Terjadi kesalahan sistem: {str(e)}"