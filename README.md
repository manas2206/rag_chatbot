# 📚 RAG Chatbot with Streaming Responses

This project is part of the **Junior AI Engineer Assignment** for **Amlgo Labs**.  
The goal is to build a **Retrieval-Augmented Generation (RAG) chatbot** that answers user queries based on a provided document.  
It supports **real-time streaming responses** via a **Streamlit interface**.

---

## 🚀 Features
- Document preprocessing and chunking (100–300 words).
- Embedding generation using **SentenceTransformers** (`all-MiniLM-L6-v2`).
- Vector database storage with **FAISS**.
- RAG pipeline (Retriever + Generator).
- Streaming responses (token-by-token like ChatGPT).
- **Streamlit UI** with:
  - Input box for natural queries.
  - Streaming answer display.
  - Sources shown under each answer.
  - Reset/clear chat option.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Transformers** (HuggingFace)
- **SentenceTransformers**
- **FAISS**
- **Streamlit**
- **PyTorch**

---

## 📂 Project Structure
rag_chatbot/
│── data/
│ └── input.txt # document used for retrieval
│── src/
│ ├── preprocess.py # document loader + chunker
│ ├── embedding.py # embedding + vector DB
│ └── generator.py # LLM + streaming
│── app.py # Streamlit chatbot app
│── requirements.txt # dependencies
│── README.md



---

## ⚙️ Setup & Installation (Windows)
1. Clone the repo:
   ```powershell
   git clone https://github.com/your-username/rag_chatbot.git
   cd rag_chatbot


2. Create virtual environment:
python -m venv rag_env
rag_env\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Deployment Link:
https://ragchatbot-manas.streamlit.app/

4. Add your document:
Place it in data/input.txt

5. Run the Chatbot
streamlit run app.py
