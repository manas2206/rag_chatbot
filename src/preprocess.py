import os
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json

DATA_PATH = "data/input.pdf"
CHUNK_PATH = "chunks/chunks.json"

def load_document(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=300, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

def save_chunks(chunks, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

if __name__ == "__main__":
    raw_text = load_document(DATA_PATH)
    chunks = chunk_text(raw_text)
    save_chunks(chunks, CHUNK_PATH)
    print(f"✅ Saved {len(chunks)} chunks to {CHUNK_PATH}")
