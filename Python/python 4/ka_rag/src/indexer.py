# src/indexer.py
import os, json, requests, numpy as np, faiss
from sentence_transformers import SentenceTransformer
from .config import *
from .normalizer import build_search_text
from .metadata import parse_age, parse_city, extract_links

os.makedirs(MODELS_DIR, exist_ok=True)

_model = None
def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(SENTENCE_MODEL)
    return _model

def fetch_knowledge():
    a = requests.get(ADMIN_API_FAQ, timeout=5).json()
    b = requests.get(ADMIN_API_DATA, timeout=5).json()
    return a + b

def build_meta_and_embeddings():
    raw = fetch_knowledge()
    meta = []
    search_texts = []
    for i, it in enumerate(raw):
        q, a = it.get("question",""), it.get("answer","")
        search_text = build_search_text(q, a)
        age = parse_age(q + " " + a)
        city = parse_city(q + " " + a)
        links = extract_links(a)
        meta.append({
            "id": i,
            "question": q,
            "answer": a,
            "age_min": age[0],
            "age_max": age[1],
            "city": city,
            "links": links,
        })
        search_texts.append(search_text)

    model = get_model()
    emb = model.encode(search_texts, convert_to_numpy=True, show_progress_bar=False)
    dim = emb.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(emb)

    faiss.write_index(index, FAISS_FILE)
    np.save(EMB_FILE, emb)
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    return meta, index, emb

def load_index():
    if not (os.path.exists(FAISS_FILE) and os.path.exists(EMB_FILE) and os.path.exists(META_FILE)):
        return build_meta_and_embeddings()
    index = faiss.read_index(FAISS_FILE)
    emb = np.load(EMB_FILE)
    with open(META_FILE, encoding="utf-8") as f:
        meta = json.load(f)
    return meta, index, emb

def rebuild_index():
    return build_meta_and_embeddings()
