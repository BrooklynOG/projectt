from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "data", "notes.txt")

with open(file_path, "r") as f:
    documents = f.read().split("\n\n")

doc_embeddings = model.encode(documents)

def load_data():
    pass

def query_data(query):
    query_emb = model.encode([query])[0]

    scores = []
    for emb in doc_embeddings:
        score = sum(q * d for q, d in zip(query_emb, emb))
        scores.append(score)

    best_idx = scores.index(max(scores))
    return documents[best_idx]
