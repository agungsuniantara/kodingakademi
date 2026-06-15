from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embeddings(texts):
    embeddings = model.encode(texts)
    return embeddings

emb1 = get_embeddings(["what is airplane"])
emb2 = get_embeddings(["can you explain airplane"])

similarity = cosine_similarity(emb1, emb2)[0][0]
print("Similarity Score :", similarity) # Similarity Score : 0.8634291