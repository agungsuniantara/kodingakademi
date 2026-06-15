from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

KNOWLEDGE_BASE = {
    "what is taman rama": "Taman Rama is an international school in Bali that provides education from kindergarten to senior high school.",
    "curriculum taman rama": "Taman Rama combines the Indonesian National Curriculum with international programs such as Cambridge Assessment.",
    "facilities taman rama": "The school has libraries, science laboratories, sports fields, music rooms, and computer labs.",
    "extracurricular activities taman rama": "Students can join sports, music, art, dance, and debate clubs."
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
    threshold = 0.80 
    
    print(f"Similarity Score: {best_score:.4f}")

    if best_score >= threshold:
        return KNOWLEDGE_BASE[kb_keys[best_index]]
    else:
        return "Sorry, I don’t understand your question"

kb_keys = list(KNOWLEDGE_BASE.keys())
kb_embeddings = get_embeddings(kb_keys)

print("Bot:", get_chatbot_response("components airplane"))