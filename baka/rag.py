from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection(name="finance")

def load_data():
    with open("data/notes.txt", "r") as f:
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