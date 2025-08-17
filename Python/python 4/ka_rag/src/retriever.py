# src/retriever.py
from typing import List, Dict, Tuple
import numpy as np
from rank_bm25 import BM25Okapi
from .config import TOP_K, BM25_K
from .normalizer import build_search_text
from .metadata import age_overlap

def build_bm25_corpus(meta: List[Dict]):
    docs = [build_search_text(m["question"], m["answer"]).split() for m in meta]
    return BM25Okapi(docs)

def faiss_search(query_emb, faiss_index, top=TOP_K):
    D, I = faiss_index.search(query_emb, top)
    return D[0], I[0]

def hybrid_search(query: str, q_emb, faiss_index, meta, bm25, filters, top=TOP_K):
    # BM25
    bm25_scores = bm25.get_scores(query.split())
    bm25_top_idx = np.argsort(bm25_scores)[-BM25_K:][::-1]

    # FAISS
    D, I = faiss_index.search(q_emb, BM25_K)
    I = I[0]                   # ⬅️  ambil baris pertama
    D = D[0]                   # ⬅️  konsistenkan juga
    faiss_scores = 1.0 / (1.0 + D)

    # Z-score
    bm25_s = (bm25_scores - np.mean(bm25_scores)) / (np.std(bm25_scores) + 1e-8)
    faiss_s = (faiss_scores - np.mean(faiss_scores)) / (np.std(faiss_scores) + 1e-8)

    # Kandidat union BM25 ∪ FAISS (flat list)
    cand = set(bm25_top_idx.tolist()) | set(I.tolist())   # ⬅️  FIX

    scores = []
    for idx in cand:
        s = bm25_s[idx] + faiss_s[np.where(I == idx)[0][0]] if idx in I else bm25_s[idx]
        # soft filter
        age_ok = age_overlap(filters.get("age_min"), filters.get("age_max"),
                             meta[idx]["age_min"], meta[idx]["age_max"])
        city_ok = (filters.get("city") is None or meta[idx]["city"] in (None, filters["city"]))
        if age_ok: s += 0.5
        if city_ok: s += 0.3
        scores.append((idx, s))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [i for i, _ in scores[:top]]
