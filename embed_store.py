import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

@st.cache_resource
def get_embedder():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(chunks):
    embeddings = get_embedder()
    vectordb = FAISS.from_documents(chunks, embeddings)
    return vectordb
