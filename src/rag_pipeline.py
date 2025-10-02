from src.retriever import retrieve
from src.generator import load_model, generate_response

def rag_pipeline(query):
    retrieved_chunks = retrieve(query, top_k=3)
    context = "\n".join(retrieved_chunks)
    model = load_model()
    response = generate_response(model, context, query)
    return response, retrieved_chunks
