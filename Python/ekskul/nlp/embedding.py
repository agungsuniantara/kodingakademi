from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

KNOWLEDGE_BASE = {
    "what is taman rama school": "Taman Rama is an international school in Bali that provides education from kindergarten to senior high school.",
    "where is taman rama located": "Taman Rama School is located in Bali, Indonesia.",
    "what curriculum does taman rama use": "Taman Rama combines the Indonesian National Curriculum with international programs such as Cambridge Assessment.",
    "what facilities does taman rama have": "The school has libraries, science laboratories, sports fields, music rooms, and computer labs.",
    "what are the extracurricular activities at taman rama": "Students can join sports, music, art, dance, and debate clubs."
}

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embeddings(texts):
    embeddings = model.encode(texts)
    return embeddings

def get_chatbot_response(user_input):
    input_emb = get_embeddings([user_input])
    similarities = cosine_similarity(input_emb, kb_embeddings)[0]
    best_index = similarities.argmax()
    best_score = similarities[best_index]
    threshold = 0.65 
    
    print(f"Similarity Score: {best_score:.4f}")

    if best_score >= threshold:
        return KNOWLEDGE_BASE[kb_keys[best_index]]
    else:
        return "Sorry, I don’t understand your question. Could you please rephrase it?"

kb_keys = list(KNOWLEDGE_BASE.keys())
kb_embeddings = get_embeddings(kb_keys)

print("Bot:", get_chatbot_response("taman rama school"))