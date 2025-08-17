# src/config.py
ADMIN_API_FAQ = "http://127.0.0.1:5001/api/knowledge_faq"
ADMIN_API_DATA = "http://127.0.0.1:5001/api/knowledge_data"

MODELS_DIR = "models"
FAISS_FILE = f"{MODELS_DIR}/faiss.index"
EMB_FILE = f"{MODELS_DIR}/embeddings.npy"
META_FILE = f"{MODELS_DIR}/meta.json"

SENTENCE_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
TOP_K = 8
BM25_K = 500
SIM_THRESHOLD = 0.35
