import os
import streamlit as st
from dotenv import load_dotenv
from ingest import load_and_chunk_pdf
from embed_store import create_vector_store
from qa_chain import get_qa_chain

load_dotenv()
st.set_page_config(page_title="📄 Research Papers Q&A Bot", layout="wide")

# Inject custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "uploaded_docs" not in st.session_state:
    st.session_state.uploaded_docs = []

st.title("🤖 Research Papers Q&A Bot")
st.caption("Ask questions from your uploaded research papers and get contextual answers!")

# Sidebar for uploading multiple PDFs
with st.sidebar:
    st.header("📚 Uploaded Papers")
    uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
    if uploaded_files:
        st.session_state.uploaded_docs = uploaded_files
        all_chunks = []
        for file in uploaded_files:
            with open(file.name, "wb") as f:
                f.write(file.read())
            chunks = load_and_chunk_pdf(file.name)
            all_chunks.extend(chunks)

        vectordb = create_vector_store(all_chunks)
        st.session_state.qa_chain = get_qa_chain(vectordb)
        st.success("✅ Documents loaded.")

        for f in uploaded_files:
            st.markdown(f"📄 **{f.name}**")

# Chat interface
for i, (question, answer) in enumerate(st.session_state.chat_history):
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        st.markdown(answer)

# Chat input + answer processing
prompt = st.chat_input("💬 Ask something:")
if prompt:
    st.session_state.chat_history.append((prompt, "⏳"))
    st.rerun()

if st.session_state.chat_history and st.session_state.chat_history[-1][1] == "⏳":
    user_question = st.session_state.chat_history[-1][0]
    if "qa_chain" in st.session_state:
        with st.spinner("🤖 Thinking..."):
            try:
                response = st.session_state.qa_chain.run(user_question)
            except Exception as e:
                response = f"❌ Error: {e}"
    else:
        response = "❗ Please upload a PDF document first."
    st.session_state.chat_history[-1] = (user_question, response)
    st.rerun()
