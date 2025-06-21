from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def get_qa_chain(vectordb):
    llm = Ollama(model="llama3")  # Running locally via Ollama
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever()
    )
