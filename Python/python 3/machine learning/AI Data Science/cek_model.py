import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_API_KEY tidak ditemukan di file .env")
else:
    print(f"✅ API Key ditemukan: {api_key[:10]}...")
    
    try:
        genai.configure(api_key=api_key)
        print("\n🔍 Sedang mencari model yang tersedia...")
        
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
                available_models.append(m.name)
        
        if not available_models:
            print("\n❌ TIDAK ADA MODEL YANG DITEMUKAN!")
            print("👉 Kemungkinan besar 'Generative Language API' belum diaktifkan di Google Cloud Console.")
        else:
            print("\n✅ Silakan gunakan salah satu nama model di atas di backend/agent.py")
            
    except Exception as e:
        print(f"\n❌ Error Koneksi: {e}")