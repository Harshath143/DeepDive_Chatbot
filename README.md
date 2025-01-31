# 🚀 DeepDive AI - PaperInsight Chatbot

DeepDive AI - PaperInsight is a powerful Streamlit-based chatbot designed to help researchers and AI enthusiasts gain in-depth insights from AI research papers. With state-of-the-art semantic search and text extraction, you can seamlessly interact with complex scientific documents.

---

## ✨ Features
✅ **Upload AI Research Papers** - Supports PDF format for easy document processing.  
✅ **Intelligent Text Extraction** - Automatically retrieves key sections and cleans text for analysis.  
✅ **Advanced Semantic Search** - Uses FAISS and Sentence Transformers to retrieve relevant information.  
✅ **AI-Powered Q&A** - Answers user queries by retrieving the most relevant content from the uploaded paper.  
✅ **Fast & Lightweight** - Optimized for performance without external API dependencies.

---

## 📌 Installation
### Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### Install Dependencies
Run the following command to install all required libraries:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage
1. **Run the chatbot**
```bash
streamlit run deepdive_chatbot_v2.py
```
2. **Upload a research paper** (PDF format).
3. **Ask a question** related to the content of the paper.
4. **Receive AI-generated responses** based on semantic search.

---

## 🛠 Tech Stack
🔹 **Text Extraction**: PyPDF2  
🔹 **Vectorization**: Sentence Transformers (`all-mpnet-base-v2`)  
🔹 **Vector Database**: FAISS for efficient search  
🔹 **AI-Powered Query Processing**: Embedding-based retrieval  
🔹 **Frontend**: Streamlit for a sleek and interactive UI

---

## 🎓 Acknowledgments
This project is inspired by **Retrieval-Augmented Generation (RAG)** methods to efficiently extract, summarize, and provide insights into AI research papers.

🌟 **Empowering researchers with AI-driven knowledge retrieval!** 🌟
