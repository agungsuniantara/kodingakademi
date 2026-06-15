import os, re, time, json, platform
import warnings
import numpy as np
import requests
import torch

from sentence_transformers import SentenceTransformer, util

# === Gunakan paket resmi langchain-ollama ===
# pip install -U langchain-ollama
try:
    from langchain_ollama import OllamaLLM
except Exception as e:
    raise RuntimeError(
        "Paket 'langchain-ollama' belum terpasang atau versi lawas. "
        "Jalankan: pip install -U langchain-ollama"
    ) from e

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core._api import LangChainDeprecationWarning  # untuk suppress warning

# =========================
# Suppress warnings (tanpa ubah flow)
# =========================
warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

# =========================
# Environment safety (hindari semaphore leak/segfault kecil)
# =========================
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
torch.set_num_threads(1)

try:
    import faiss  # opsional; bisa crash di beberapa build macOS
    FAISS_AVAILABLE = True
except Exception:
    FAISS_AVAILABLE = False

# =========================
# Konfigurasi
# =========================
FAQ_API_URL   = "http://127.0.0.1:5000/api/knowledge_faq"
PROGRAMS_API  = "http://127.0.0.1:5000/api/knowledge_data"

CACHE_DURATION     = 300
SIM_THRESHOLD_RAG  = 0.35
TOP_K              = 5

FAQ_HARD_THRESHOLD = 0.60
FAQ_SOFT_THRESHOLD = 0.45

INDEX_FILE      = "faiss.index"
EMBEDDINGS_FILE = "embeddings.npy"
DOCS_FILE       = "docs.json"

IS_MAC = platform.system().lower() == "darwin"
USE_FAISS = FAISS_AVAILABLE and (not IS_MAC)

DEVICE = "cpu"

_sentence_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
_sentence_model.to(DEVICE)

_dynamic_cache = {
    "last_update": 0,
    "faiss_index": None,
    "embeddings": None,
    "docs": None,
    "raw": None,
    "faq_qs": None,
    "faq_qs_emb": None,
}

CITY_KEYWORDS = {
    "denpasar": "Denpasar",
    "gianyar": "Gianyar",
    "surabaya": "Surabaya"
}

# =========================
# Simple drop-in replacement for ConversationBufferMemory
# =========================
class SimpleBufferMemory:
    """API yang dipakai kode ini:
       - load_memory_variables({}) -> {"history": List[HumanMessage|AIMessage]}
       - save_context({"input": ...}, {"output": ...}) -> append ke history
    """
    def __init__(self, return_messages: bool = True):
        self.return_messages = return_messages
        self._history = []  # list of HumanMessage / AIMessage

    def load_memory_variables(self, _: dict) -> dict:
        return {"history": list(self._history)}

    def save_context(self, input_dict: dict, output_dict: dict) -> None:
        user_text = input_dict.get("input", "")
        bot_text  = output_dict.get("output", "")
        if user_text:
            self._history.append(HumanMessage(content=user_text))
        if bot_text:
            self._history.append(AIMessage(content=bot_text))

# =========================
# Helper ambil data
# =========================
def get_programs():
    try:
        return requests.get(PROGRAMS_API, timeout=5).json()
    except Exception as e:
        print("Error ambil programs:", e)
        return []

def get_faq():
    try:
        return requests.get(FAQ_API_URL, timeout=5).json()
    except Exception as e:
        print("Error ambil FAQ:", e)
        return []

def build_docs_for_embedding(programs, faq):
    docs = []
    for p in programs:
        name = p.get("name","")
        cat  = p.get("category","")
        min_age = p.get("min_age")
        max_age = p.get("max_age")
        range_txt = f"{min_age}+" if (max_age in (None, "", 0)) else f"{min_age}–{max_age}"
        desc = p.get("description","")
        video = p.get("video","")
        locs = p.get("locations",{})
        links_all = "\n".join([f"- {k}: {v}" for k,v in locs.items()]) if locs else ""
        block = f"""PROGRAM:
Nama: {name}
Kategori: {cat}
Usia: {range_txt}
Deskripsi: {desc}
Video: {video}
Link:
{links_all}
"""
        docs.append(block)
    for f in faq:
        q = f.get("question","")
        a = f.get("answer","")
        docs.append(f"FAQ:: {q}\n{a}")
    return docs

# =========================
# FAISS utils (opsional)
# =========================
def _norm_f32(a: np.ndarray) -> np.ndarray:
    if a.dtype != np.float32:
        a = a.astype(np.float32, copy=False)
    a = np.ascontiguousarray(a)
    norms = np.linalg.norm(a, axis=1, keepdims=True) + 1e-12
    a = a / norms
    return a

def save_index_and_embeddings(index, embeddings, docs):
    import faiss
    faiss.write_index(index, INDEX_FILE)
    np.save(EMBEDDINGS_FILE, embeddings)
    with open(DOCS_FILE, "w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=0)

def load_index_and_embeddings():
    if os.path.exists(INDEX_FILE) and os.path.exists(EMBEDDINGS_FILE) and os.path.exists(DOCS_FILE):
        import faiss
        index = faiss.read_index(INDEX_FILE)
        embeddings = np.load(EMBEDDINGS_FILE)
        with open(DOCS_FILE, "r", encoding="utf-8") as f:
            docs = json.load(f)
        return index, embeddings, docs
    return None, None, None

def build_faiss_index_IP(embeddings):
    import faiss
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    return index

# =========================
# Cache builder
# =========================
def ensure_faq_question_embeddings(faq):
    qs = [ (item.get("question","") or "").strip() for item in faq ]
    if not qs:
        _dynamic_cache["faq_qs"] = []
        _dynamic_cache["faq_qs_emb"] = None
        return
    emb = _sentence_model.encode(qs, convert_to_tensor=True)
    _dynamic_cache["faq_qs"] = qs
    _dynamic_cache["faq_qs_emb"] = emb

def load_all_and_build_if_needed():
    now = time.time()
    need_update = (now - _dynamic_cache["last_update"] > CACHE_DURATION) or (_dynamic_cache["docs"] is None)

    if need_update:
        programs = get_programs()
        faq = get_faq()
        ensure_faq_question_embeddings(faq)

        docs = build_docs_for_embedding(programs, faq)
        if not docs:
            print("Tidak ada knowledge yang tersedia!")
            _dynamic_cache.update({"raw": {"programs": programs, "faq": faq}, "docs": [], "faiss_index": None})
            return _dynamic_cache["raw"], _dynamic_cache["docs"], _dynamic_cache["faiss_index"]

        embs = _sentence_model.encode(docs, convert_to_numpy=True, show_progress_bar=False)
        if USE_FAISS:
            try:
                embs_n = _norm_f32(embs)
                index = build_faiss_index_IP(embs_n)
                save_index_and_embeddings(index, embs_n, docs)
                _dynamic_cache["faiss_index"] = index
                _dynamic_cache["embeddings"] = embs_n
            except Exception as e:
                print("Peringatan: FAISS gagal, fallback ke NumPy cosine. Err:", e)
                _dynamic_cache["faiss_index"] = None
                _dynamic_cache["embeddings"] = _norm_f32(embs)
        else:
            _dynamic_cache["faiss_index"] = None
            _dynamic_cache["embeddings"] = _norm_f32(embs)

        _dynamic_cache.update({
            "last_update": now,
            "docs": docs,
            "raw": {"programs": programs, "faq": faq}
        })

    else:
        if USE_FAISS and _dynamic_cache["faiss_index"] is None:
            try:
                index, embs, docs_disk = load_index_and_embeddings()
                if index is not None:
                    _dynamic_cache["faiss_index"] = index
                    _dynamic_cache["embeddings"] = embs
                    _dynamic_cache["docs"] = docs_disk
            except Exception as e:
                print("Load FAISS index gagal, tetap pakai cache memori. Err:", e)

    return _dynamic_cache["raw"], _dynamic_cache["docs"], _dynamic_cache["faiss_index"]

# =========================
# Ekstraksi usia & kota & salam
# =========================
def extract_age(text):
    m = re.search(r'(?:umur|usia)\s*(\d{1,2})', text.lower())
    if m:
        return int(m.group(1))
    m2 = re.search(r'\b([4-9]|1[0-9])\b', text)
    return int(m2.group(1)) if m2 else None

def extract_city(text):
    lower = text.lower()
    for k, v in CITY_KEYWORDS.items():
        if k in lower:
            return v
    return None

def extract_greeting(query):
    lower = query.lower()
    if "selamat pagi"  in lower: return "Selamat pagi"
    if "selamat siang" in lower: return "Selamat siang"
    if "selamat sore"  in lower: return "Selamat sore"
    if "selamat malam" in lower: return "Selamat malam"
    if any(w in lower for w in ["halo","hai","hello"]): return "Halo"
    return None

# =========================
# Jalur deterministik: PROGRAM by age
# =========================
def filter_programs_by_age_city(programs, age, city=None):
    def fits(p):
        min_ok = (p.get("min_age") is None) or (age >= p["min_age"])
        maxv = p.get("max_age")
        max_ok = (maxv is None) or (age <= maxv)
        return min_ok and max_ok

    eligible = [p for p in programs if fits(p)]
    eligible.sort(key=lambda x: (x.get("min_age") or 0, x.get("name","")))

    def fmt_line(p):
        min_age, max_age = p.get("min_age"), p.get("max_age")
        range_txt = f"{min_age}+" if max_age in (None, "", 0) else f"{min_age}–{max_age}"
        locs = p.get("locations",{})
        pref = []
        if city and city in locs:
            pref.append(f"{city}: {locs[city]}")
        others = [f"{k}: {v}" for k,v in locs.items() if not (city and k==city)]
        link_block = ""
        if pref or others:
            link_block = " — " + " | ".join(pref + others)
        return f"• {p['name']} (usia {range_txt}){link_block}"

    return eligible, [fmt_line(p) for p in eligible]

def reply_for_age(programs, age, city, greeting):
    eligible, lines = filter_programs_by_age_city(programs, age, city)
    if eligible:
        head = f"{greeting+'! ' if greeting else ''}Pilihan program untuk usia {age}:"
        return "\n".join([head, ""] + lines)

    higher = sorted([p for p in programs if (p.get('min_age') or 0) > age],
                    key=lambda x: x.get('min_age') or 0)
    lower  = sorted([p for p in programs if (p.get('min_age') or 0) <= age],
                    key=lambda x: x.get('min_age') or 0, reverse=True)
    near = (higher[:3] or lower[:3])
    if not near:
        return f"{greeting+'! ' if greeting else ''}Belum ada program untuk usia {age}."
    head = f"{greeting+'! ' if greeting else ''}Belum ada yang pas untuk usia {age}. Ini yang paling dekat:"
    lines = []
    for p in near:
        min_age, max_age = p.get("min_age"), p.get("max_age")
        range_txt = f"{min_age}+" if max_age in (None, "", 0) else f"{min_age}–{max_age}"
        any_link = next(iter(p.get("locations",{}).values()), None)
        link_txt = f" — {any_link}" if any_link else ""
        lines.append(f"• {p['name']} (usia {range_txt}){link_txt}")
    return "\n".join([head, ""] + lines)

# =========================
# Jalur deterministik: FAQ
# =========================
def is_address_intent(text):
    lower = text.lower()
    return any(w in lower for w in ["alamat", "lokasi", "dimana", "di mana", "ada di", "di denpasar", "di gianyar", "di surabaya"])

def faq_direct_match(query, faq):
    greeting = extract_greeting(query)
    city = extract_city(query)

    if is_address_intent(query) and city:
        target_key = f"koding akademi {city.lower()}"
        for item in faq:
            q = (item.get("question","") or "").lower()
            if target_key in q:
                ans = (item.get("answer","") or "").strip()
                if not ans:
                    continue
                head = f"{greeting+'! ' if greeting else ''}Alamat Koding Akademi di {city}:"
                return {"mode":"direct", "text": f"{head}\n{ans}"}
        head = f"{greeting+'! ' if greeting else ''}Alamat untuk {city} belum tersedia di data."
        return {"mode":"direct", "text": head}

    qs = _dynamic_cache.get("faq_qs") or []
    qembs = _dynamic_cache.get("faq_qs_emb")
    if qs and qembs is not None:
        q_emb = _sentence_model.encode([query], convert_to_tensor=True)
        sims = util.cos_sim(q_emb, qembs)[0].detach().cpu().numpy()
        best_idx = int(np.argmax(sims))
        best_score = float(sims[best_idx])
        best_ans = (faq[best_idx].get("answer","") or "").strip()
        if best_score >= FAQ_HARD_THRESHOLD and best_ans:
            if greeting:
                return {"mode":"direct", "text": f"{greeting}!\n\n{best_ans}"}
            return {"mode":"direct", "text": best_ans}
        elif best_score >= FAQ_SOFT_THRESHOLD and best_ans:
            return {"mode":"soft", "idx": best_idx, "score": best_score, "answer": best_ans}
    return None

# =========================
# Retrieval (FAISS atau NumPy)
# =========================
def retrieve(query, docs, embeddings, faiss_index=None, top_k=TOP_K):
    if faiss_index is not None and USE_FAISS:
        q = _sentence_model.encode([query], convert_to_numpy=True)
        q = _norm_f32(q)
        D, I = faiss_index.search(q, top_k)
        sims = D[0]
        idxs = I[0]
        return [docs[i] for i in idxs], idxs, sims
    q = _sentence_model.encode([query], convert_to_numpy=True)
    q = _norm_f32(q)[0]
    M = embeddings.T
    sims = q @ M
    top_idx = np.argsort(-sims)[:top_k]
    return [docs[i] for i in top_idx], top_idx, sims[top_idx]

# =========================
# Prompt builder
# =========================
def build_full_prompt(memory, context, query, extra_instruksi=""):
    history_payload = memory.load_memory_variables({}).get("history", [])
    history_txt = ""
    if isinstance(history_payload, list):
        for msg in history_payload:
            if isinstance(msg, HumanMessage):
                history_txt += f"Pengguna: {msg.content}\n"
            elif isinstance(msg, AIMessage):
                history_txt += f"Bot: {msg.content}\n"
    elif isinstance(history_payload, str):
        history_txt = history_payload

    prompt = f"""
Kamu adalah staf Koding Akademi yang ramah.
Jawab singkat, jelas, santai (Bahasa Indonesia).
Gunakan HANYA info pada 'Pengetahuan'. DILARANG membuat link/program baru.
Jika link tidak ada di Pengetahuan, tulis 'link tidak tersedia'.
Jika beberapa program/opsi cocok, sebutkan semuanya yang ADA di Pengetahuan.
Jangan sebut AI/pengetahuan/referensi, dan jangan pakai bridging. {extra_instruksi}
Jangan jawab tidak ada di pengetahuan, bisa jawab silahkan menghubungi admin.

Riwayat:
{history_txt}

Pengetahuan:
{context}

Pertanyaan:
{query}

Jawaban:
"""
    return prompt

# =========================
# Main chatbot
# =========================
def chatbot():
    llm = OllamaLLM(model="llama3:8b")
    memory = SimpleBufferMemory(return_messages=True)

    print("=== Chatbot Koding Akademi (Programs by Age + Deterministic FAQ + RAG) ===")
    print("Ketik 'exit' untuk keluar.\n")

    while True:
        try:
            query = input("You: ").strip()
        except EOFError:
            break

        if not query or query.lower() == "exit":
            break

        raw, docs, _ = load_all_and_build_if_needed()
        programs = raw.get("programs", [])
        faq = raw.get("faq", [])
        embeddings = _dynamic_cache["embeddings"]
        faiss_index = _dynamic_cache["faiss_index"] if USE_FAISS else None

        greeting = extract_greeting(query)
        age = extract_age(query)
        city = extract_city(query)

        # 1) Jalur deterministik: program by age
        if age is not None and programs:
            answer = reply_for_age(programs, age, city, greeting)
            print("Bot:", answer.strip())
            memory.save_context({"input": query}, {"output": answer})
            continue

        # 2) Jalur deterministik: FAQ direct match
        soft_faq_context = None
        if faq:
            faq_try = faq_direct_match(query, faq)
            if faq_try and faq_try.get("mode") == "direct":
                print("Bot:", faq_try["text"].strip())
                memory.save_context({"input": query}, {"output": faq_try["text"]})
                continue
            soft_faq_context = faq_try if faq_try and faq_try.get("mode") == "soft" else None

        # 3) Fallback RAG
        if not docs or embeddings is None:
            print("Bot: Knowledge tidak tersedia, silakan cek API!")
            continue

        contexts, indices, scores = retrieve(query, docs, embeddings, faiss_index, top_k=TOP_K)
        kept = [(i, s) for i, s in zip(indices, scores) if s >= SIM_THRESHOLD_RAG]
        if not kept:
            kept = [(indices[0], scores[0])]

        rag_blocks = []
        if soft_faq_context:
            rag_blocks.append(f"FAQ-KANDIDAT:\n{soft_faq_context['answer']}")
        rag_blocks += [docs[i] for i, _ in kept]
        combined_context = "\n\n".join(rag_blocks)

        extra = f"\nBalas salam '{greeting}' di awal." if greeting else ""
        prompt = build_full_prompt(memory, combined_context, query, extra)
        answer = llm.invoke(prompt)

        print("Bot:", answer.strip())
        memory.save_context({"input": query}, {"output": answer})

if __name__ == "__main__":
    chatbot()
