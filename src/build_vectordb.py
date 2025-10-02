import os
import json
from sentence_transformers import SentenceTransformer
import chromadb

CHUNK_PATH = "chunks/chunks.json"
VECTORDB_PATH = "vectordb"

def build_vectordb():
    # Load chunks
    with open(CHUNK_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    # Embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Init ChromaDB
    os.makedirs(VECTORDB_PATH, exist_ok=True)
    client = chromadb.PersistentClient(path=VECTORDB_PATH)
    collection = client.create_collection("docs")

    for i, chunk in enumerate(chunks):
        embedding = model.encode([chunk])[0].tolist()
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embedding]
        )

    print(f"✅ Stored {len(chunks)} chunks in vector DB")

if __name__ == "__main__":
    build_vectordb()
