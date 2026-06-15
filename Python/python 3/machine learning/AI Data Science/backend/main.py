import os
import shutil
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.agent import get_agent_response

app = FastAPI(title="InsightAI API")

# Setup CORS agar Streamlit (Port 8501) bisa akses FastAPI (Port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pastikan folder data ada
os.makedirs("data", exist_ok=True)

@app.get("/")
def read_root():
    return {"status": "Server is running", "service": "InsightAI Backend"}

@app.post("/analyze")
async def analyze_data(file: UploadFile = File(...), query: str = Form(...)):
    """
    Endpoint utama: Menerima File CSV + Pertanyaan Text
    """
    file_path = f"data/{file.filename}"
    
    try:
        # 1. Simpan file upload ke server lokal
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # 2. Panggil Agent AI untuk memproses
        result_text = get_agent_response(file_path, query)
        
        # 3. Return hasil
        return {"filename": file.filename, "answer": result_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    finally:
        # Opsional: Hapus file setelah diproses untuk hemat storage
        # if os.path.exists(file_path):
        #     os.remove(file_path)
        pass

if __name__ == "__main__":
    import uvicorn
    # Jalankan server
    uvicorn.run(app, host="0.0.0.0", port=8000)