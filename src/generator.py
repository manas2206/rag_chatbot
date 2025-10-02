# generator.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Use a lightweight CPU-friendly model
MODEL_NAME = "google/flan-t5-base"

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_response(model, context, query, max_new_tokens=200):
    prompt = f"""
    You are a helpful assistant. Use the following context to answer the question.

    Context:
    {context}

    Question: {query}
    Answer:
    """
    output = model(prompt, max_new_tokens=max_new_tokens)
    return output[0]["generated_text"]
