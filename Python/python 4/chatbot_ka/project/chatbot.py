import json
import time
import os
import numpy as np
import faiss
import requests
from sentence_transformers import SentenceTransformer
from langchain_ollama import OllamaLLM
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

FAQ_API_URL = "http://127.0.0.1:5000/api/knowledge_faq"
DATA_API_URL = "http://127.0.0.1:5000/api/knowledge_data"
CACHE_DURATION = 0
SIM_THRESHOLD = 0.35
TOP_K = 5

# File persistence
INDEX_FILE = "faiss.index"
EMBEDDINGS_FILE = "embeddings.npy"
DOCS_FILE = "docs.json"

_sentence_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
_dynamic_cache = {
    "static": [],
    "dynamic": [],
    "last_update": 0,
    "faiss_index": None,
    "embeddings": None,
    "docs": None,
    "data": None
}

def get_knowledge_from_api():
    try:
        static = requests.get(FAQ_API_URL, timeout=5).json()
        dynamic = requests.get(DATA_API_URL, timeout=5).json()
        return static + dynamic
    except Exception as e:
        print("Error ambil knowledge:", e)
        return []

def save_index_and_embeddings(index, embeddings, docs):
    faiss.write_index(index, INDEX_FILE)
    np.save(EMBEDDINGS_FILE, embeddings)
    with open(DOCS_FILE, "w", encoding="utf-8") as f:
        json.dump(docs, f)

def load_index_and_embeddings():
    if os.path.exists(INDEX_FILE) and os.path.exists(EMBEDDINGS_FILE) and os.path.exists(DOCS_FILE):
        index = faiss.read_index(INDEX_FILE)
        embeddings = np.load(EMBEDDINGS_FILE)
        with open(DOCS_FILE, "r", encoding="utf-8") as f:
            docs = json.load(f)
        return index, embeddings, docs
    return None, None, None

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def load_all_knowledge_and_faiss():
    now = time.time()
    # Ambil ulang knowledge jika expired atau index belum ada
    need_update = (now - _dynamic_cache["last_update"] > CACHE_DURATION)
    data = get_knowledge_from_api() if need_update else _dynamic_cache.get("data", [])
    docs = [f"{item['question']} {item['answer']}" for item in data]
    if (need_update or _dynamic_cache["faiss_index"] is None or
        _dynamic_cache["docs"] != docs):
        if len(docs) == 0:
            print("Tidak ada knowledge yang tersedia!")
            return [], [], None
        # Build new embeddings & index
        embeddings = _sentence_model.encode(docs, convert_to_numpy=True, show_progress_bar=False)
        index = build_faiss_index(embeddings)
        save_index_and_embeddings(index, embeddings, docs)
        _dynamic_cache.update({
            "faiss_index": index,
            "embeddings": embeddings,
            "docs": docs,
            "data": data,
            "last_update": now
        })
    else:
        # Try load from disk for fast startup
        index, embeddings, docs_disk = load_index_and_embeddings()
        if index is not None and docs_disk == docs:
            _dynamic_cache.update({
                "faiss_index": index,
                "embeddings": embeddings,
                "docs": docs_disk,
            })
        else:
            # Fallback: build index from memory cache
            embeddings = _dynamic_cache["embeddings"]
            index = build_faiss_index(embeddings)
            _dynamic_cache["faiss_index"] = index
        data = _dynamic_cache["data"]
        docs = _dynamic_cache["docs"]
    return data, docs, _dynamic_cache["faiss_index"]

def retrieve_semantic_faiss(query, docs, faiss_index, model, top_k=TOP_K):
    query_emb = model.encode([query], convert_to_numpy=True)
    D, I = faiss_index.search(query_emb, top_k)
    I = I[0]
    scores = 1 / (1 + D[0])   # Convert L2 distance to a "score" (0..1)
    return [docs[idx] for idx in I], I, scores

def build_full_prompt(memory, context, query):
    history_messages = memory.load_memory_variables({})["history"]
    history_txt = ""
    for msg in history_messages:
        if isinstance(msg, HumanMessage):
            history_txt += f"Pengguna: {msg.content}\n"
        elif isinstance(msg, AIMessage):
            history_txt += f"Bot: {msg.content}\n"
    prompt = f"""
Kamu adalah staf Koding Akademi yang ramah dan profesional. 
Jawablah pertanyaan pengguna di bawah ini hanya dengan informasi dari bagian Pengetahuan, 
dan jawab HANYA dalam bahasa Indonesia sehari-hari, singkat, jelas, dan tidak formal.
Jika jawaban sudah jelas di Pengetahuan, langsung tampilkan apa adanya.
Jangan pernah menjawab dalam bahasa lain selain bahasa yang digunakan untuk bertanya.
Jangan pernah menyebut atau menyinggung bahwa kamu adalah AI, chatbot, mesin, atau menyebut kata 'referensi', 'pengetahuan', 
atau 'berdasarkan informasi'. 
Berikan seluruh pilihan produk apabila persyaratan memenuhi lebih dari 1 produk.
Jangan memulai jawaban dengan kalimat pembuka seperti 'Menurut', 'Berdasarkan', 'Saya menemukan', atau yang serupa. 
**Jangan gunakan kata pembuka bridging seperti 'Baik,', 'Kembali,', 'Next', atau pengalihan topik, jawab langsung ke inti jawaban tanpa bridging.**
Fokus langsung pada inti jawaban seperti manusia biasa yang sedang melayani calon murid.

Jika jawaban tidak ada di pengetahuan, cukup jawab dengan sopan dan arahkan ke admin atau website resmi Koding Akademi tanpa embel-embel AI.

Riwayat percakapan:
{history_txt}

Pengetahuan:
{context}

Pertanyaan:
{query}

Jawaban:
"""
    return prompt

def chatbot():
    llm = OllamaLLM(model="llama3:8b")
    memory = ConversationBufferMemory(return_messages=True)
    model = _sentence_model

    print("=== RAG Chatbot + SBERT + FAISS Semantic Search + Index Persistence ===")
    print("Tanya apa saja tentang Koding Akademi! (Ketik 'exit' untuk keluar)\n")

    while True:
        query = input("You: ").strip().lower()
        if not query or query.lower() == "exit":
            break

        # Ambil data & index FAISS (persistence-aware)
        data, docs, faiss_index = load_all_knowledge_and_faiss()
        if not data or not docs or faiss_index is None:
            print("Bot: Knowledge tidak tersedia, silakan cek API/knowledgebase!")
            continue

        # Cari Top-K via FAISS
        contexts, indices, scores = retrieve_semantic_faiss(query, docs, faiss_index, model, top_k=TOP_K)
        print("\n[Debug] Semantic Similarity (FAISS) & Context Retrieved:")
        for i, (idx, sc) in enumerate(zip(indices, scores)):
            info = f"  Top-{i+1} (score={sc:.3f}): Q: {data[idx]['question'][:50]}... | A: {data[idx]['answer'][:50]}..."
            print(info)
        print("-" * 60)

        # Ambil minimal 1 context paling relevan (jika ada yang di atas threshold)
        if any(score >= SIM_THRESHOLD for score in scores):
            combined_context = "\n".join(
                [data[idx]["answer"] for i, idx in enumerate(indices) if scores[i] >= SIM_THRESHOLD]
            )
        else:
            combined_context = data[indices[0]]["answer"]

        prompt = build_full_prompt(memory, combined_context, query)
        answer = llm.invoke(prompt)
        print("Bot:", answer.strip())
        memory.save_context({"input": query}, {"output": answer})

if __name__ == "__main__":
    chatbot()