from sentence_transformers import SentenceTransformer
import chromadb
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection(name="finance")

def load_data():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "data", "notes.txt")

    with open(file_path, "r") as f:
        texts = f.read().split("\n\n")

    embeddings = model.encode(texts)

    for i, text in enumerate(texts):
        collection.add(
            documents=[text],
            embeddings=[embeddings[i].tolist()],
            ids=[str(i)]
        )

def query_data(query):
    q_emb = model.encode([query]).tolist()
    results = collection.query(query_embeddings=q_emb, n_results=2)

    docs = results.get("documents", [[]])[0]
    return " ".join(docs) if docs else ""
