# 📄 Research Papers Q&A Bot

An interactive chatbot built with Streamlit that allows you to **upload research papers (PDFs)** and ask questions in a **ChatGPT-style interface**. It uses **local LLMs via Ollama**, text embeddings, and **vector search with FAISS** to generate contextual, accurate answers from your documents.

---

## 🚀 Features

- 📁 Upload **one or multiple** research papers (PDF)
- ✂️ Automatic **text chunking and preprocessing**
- 🧠 **FAISS** vector store for fast similarity search
- 🤖 Q&A using **Ollama LLMs** (e.g., `llama3`)
- 💬 Chat-like interface with conversation history
- 🖼️ Modern and responsive **Streamlit UI**
- 🧹 Clear chat and 💾 download Q&A history
- 🔐 `.env` excluded for secure key management

---

## 🛠️ Project Structure

```
research-paper-qa-bot/
├── app.py              # Main Streamlit app
├── style.css           # UI styling
├── qa_chain.py         # Builds the QA chain with LLM + retriever
├── embed_store.py      # Embedding & vector DB creation
├── ingest.py           # PDF loading & chunking
├── utils.py            # Helper functions
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Meghashyam-adimallam/Research-paper-qa-bot.git
cd Research-paper-qa-bot
```

### 2. Install Python packages

```bash
pip install -r requirements.txt
```

### 3. Install Ollama (for local LLM inference)

Install Ollama from [https://ollama.com](https://ollama.com) and run:

```bash
ollama run llama3
```

This ensures the `llama3` model is running at `http://localhost:11434`.

### 4. Set up your `.env` file

Create a `.env` file in the root directory with:

```
OLLAMA_BASE_URL=http://localhost:11434
```

> 🔐 This is excluded from GitHub with `.gitignore` for security.

### 5. Launch the app

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. **Upload PDFs** → Extracts and chunks text using PyMuPDF.
2. **Embeddings** → Uses `all-MiniLM-L6-v2` to vectorize chunks.
3. **Vector Search** → Uses FAISS to retrieve relevant content.
4. **Answering** → Local LLM (e.g. `llama3` via Ollama) generates answers using retrieved context.
5. **UI** → Modern, chat-style interface powered by Streamlit.

---

## 📎 Example Use Cases

* Understand complex academic papers quickly
* Summarize key ideas from uploaded research
* Ask follow-up or deep-dive questions across multiple documents

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

* [Ollama](https://ollama.com/) for fast local LLM inference
* [LangChain](https://www.langchain.com/) for chaining embeddings + LLM
* [FAISS](https://github.com/facebookresearch/faiss) for vector search
* [Streamlit](https://streamlit.io/) for the beautiful UI

---

> Made with 💻 and 🔍 by Megha
