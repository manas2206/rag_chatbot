import chromadb

VECTORDB_PATH = "vectordb"

def get_retriever():
    client = chromadb.PersistentClient(path=VECTORDB_PATH)
    return client.get_collection("docs")

def retrieve(query, top_k=3):
    collection = get_retriever()
    results = collection.query(query_texts=[query], n_results=top_k)
    return results["documents"][0]
