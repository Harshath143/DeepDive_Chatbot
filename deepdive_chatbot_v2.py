import streamlit as st
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import PyPDF2
import re

# Load the embedding model (optimized for accuracy and speed)
embed_model = SentenceTransformer("all-mpnet-base-v2")

# Initialize FAISS index
index = faiss.IndexFlatL2(768)  # 768-dimensional embeddings
stored_texts = []  # Store original text snippets

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to clean and preprocess text
def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    return text.strip()

# Function to chunk text efficiently
def chunk_text(text, chunk_size=500):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# Streamlit UI
st.set_page_config(page_title="DeepDive AI - PaperInsight Chatbot", layout="wide")
st.title("📄 DeepDive AI - PaperInsight Chatbot")
st.markdown("Upload an AI Research Paper and get instant insights!")

# File uploader
uploaded_file = st.file_uploader("Upload an AI Research Paper (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("🔄 Processing PDF..."):
        paper_text = extract_text_from_pdf(uploaded_file)
        cleaned_text = preprocess_text(paper_text)
        text_chunks = chunk_text(cleaned_text)
        embeddings = embed_model.encode(text_chunks, convert_to_numpy=True)
        
        global stored_texts, index
        stored_texts = text_chunks  # Store chunks for retrieval
        index = faiss.IndexFlatL2(768)
        index.add(np.array(embeddings))
    
    st.success("✅ PDF Processed! You can now ask questions.")
    
    user_query = st.text_input("🔍 Ask a question about the paper:")
    
    if user_query:
        query_embedding = embed_model.encode([user_query], convert_to_numpy=True)
        D, I = index.search(np.array(query_embedding), k=5)  # Retrieve top 5 matches
        
        response = "\n".join([stored_texts[i] for i in I[0] if i < len(stored_texts)])
        
        st.markdown("### 📝 Answer:")
        st.write(response)
