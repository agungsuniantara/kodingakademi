from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embeddings(texts):
    embeddings = model.encode(texts)
    return embeddings

emb1 = get_embeddings(["what is airplane"])
emb2 = get_embeddings(["can you explain airplane"])

print("Shape of emb1 :", emb1.shape) # (1, 384)
print("Shape of emb2 :", emb2.shape) # (1, 384)