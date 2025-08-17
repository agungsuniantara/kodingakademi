# src/chat_api.py
from fastapi import FastAPI, Body
from pydantic import BaseModel
import numpy as np, faiss, os, json
from sentence_transformers import SentenceTransformer
from langchain_ollama import OllamaLLM
from langchain.memory import ConversationBufferMemory
from .config import *
from .indexer import load_index, rebuild_index, get_model
from .retriever import build_bm25_corpus, hybrid_search
from .intent import extract_greeting, parse_filters, extract_topic
from .templates_ import format_program_list, address_answer
from .prompt import build_prompt

app = FastAPI(title="Koding Akademi RAG Chat")
meta, faiss_index, emb = load_index()
bm25 = build_bm25_corpus(meta)
st_model = get_model()
llm = OllamaLLM(model="llama3:8b")
memory = ConversationBufferMemory(return_messages=True)

class ChatIn(BaseModel):
    query: str

@app.post("/chat")
def chat(inp: ChatIn):
    global meta, faiss_index, emb, bm25
    q = inp.query.strip()
    greeting = extract_greeting(q)
    filters = parse_filters(q)
    topic = extract_topic(q)

    # routing deterministik untuk alamat
    if topic == "address" and filters.get("city"):
        city = filters["city"]
        candidates = [m for m in meta if m.get("city")==city and "alamat" in (m["question"]+" "+m["answer"]).lower()]
        answer = address_answer(candidates, city)
        if greeting: answer = f"{greeting}!\n\n{answer}"
        return {"answer": answer}

    # hybrid retrieve
    q_emb = st_model.encode([q], convert_to_numpy=True)
    top_ids = hybrid_search(q, q_emb, faiss_index, meta, bm25, filters, top=TOP_K)
    items = [meta[i] for i in top_ids]

    # context terstruktur
    structured = format_program_list(items)
    # history text singkat
    hist = ""
    for m in memory.chat_memory.messages[-6:]:  # tail
        role = "Pengguna" if m.type=="human" else "Bot"
        hist += f"{role}: {m.content}\n"

    prompt = build_prompt(hist, structured, q, greeting)
    if not items:
        # kosong → jawaban fallback
        ans = (f"{greeting+'! ' if greeting else ''}Maaf, belum ada info yang pas. "
               f"Silakan hubungi admin Koding Akademi ya!")
        memory.save_context({"input": q}, {"output": ans})
        return {"answer": ans}

    out = llm.invoke(prompt).strip()
    memory.save_context({"input": q}, {"output": out})
    return {"answer": out}

# webhook rebuild (dipanggil admin saat Save)
@app.post("/admin/rebuild")
def admin_rebuild():
    global meta, faiss_index, emb, bm25
    meta, faiss_index, emb = rebuild_index()
    bm25 = build_bm25_corpus(meta)
    return {"status":"ok","items":len(meta)}

if __name__ == "__main__":
    import uvicorn
    os.makedirs(MODELS_DIR, exist_ok=True)
    uvicorn.run("src.chat_api:app", host="0.0.0.0", port=8001, reload=True)
