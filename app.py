import streamlit as st
from src.rag_pipeline import rag_pipeline

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("📘 Fine-Tuned RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

if user_input := st.chat_input("Ask your question..."):
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("🤔 Thinking...")

        response, sources = rag_pipeline(user_input)

        final_answer = f"{response}\n\n**Sources Used:**\n- " + "\n- ".join(sources)
        placeholder.markdown(final_answer)

        st.session_state["messages"].append({"role": "assistant", "content": final_answer})
