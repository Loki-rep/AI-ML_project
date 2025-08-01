import os
import faiss
import pickle
import requests
import numpy as np
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -------------------------------
# STEP 1: Extract Text from PDF
# -------------------------------
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# -------------------------------
# STEP 2: Chunk the text
# -------------------------------
def chunk_text(text, chunk_size=300):
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

# -------------------------------
# STEP 3: Build & Save FAISS Index
# -------------------------------
def build_and_save_faiss_index(chunks, model, index_path="faiss.index", metadata_path="metadata.pkl"):
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    faiss.write_index(index, index_path)
    with open(metadata_path, "wb") as f:
        pickle.dump(chunks, f)
    print("✅ FAISS index and metadata saved.")

# -------------------------------
# STEP 4: Load FAISS & Metadata
# -------------------------------
def load_faiss_index(index_path="faiss.index", metadata_path="metadata.pkl"):
    index = faiss.read_index(index_path)
    with open(metadata_path, "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

# -------------------------------
# STEP 5: Retrieve Relevant Chunks
# -------------------------------
def retrieve_chunks_faiss(query, model, index, chunks, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in indices[0]]

# -------------------------------
# STEP 6: Generate Answer with Groq
# -------------------------------
def generate_with_groq(prompt, groq_api_key):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    try:
        data = response.json()
        print("🧾 Full Response from Groq:\n", data)

        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"]
        else:
            return "❌ No choices returned by Groq. Check your API key or prompt."
    except Exception as e:
        return f"❌ Error decoding Groq response: {e}"

# -------------------------------
# STEP 7: Main RAG Workflow
# -------------------------------
def build_index_from_pdf(pdf_path, index_path="faiss.index", metadata_path="metadata.pkl"):
    print("📄 Reading PDF...")
    text = extract_text_from_pdf(pdf_path)
    print("✂️ Chunking...")
    chunks = chunk_text(text)
    print("🔍 Embedding and building index...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    build_and_save_faiss_index(chunks, model, index_path, metadata_path)

def query_rag(query, groq_api_key, index_path="faiss.index", metadata_path="metadata.pkl", top_k=3):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    index, chunks = load_faiss_index(index_path, metadata_path)
    top_chunks = retrieve_chunks_faiss(query, model, index, chunks, top_k)
    context = "\n\n---\n\n".join(top_chunks)
    prompt = f"Use the context below to answer the question.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
    return generate_with_groq(prompt, groq_api_key)

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    PDF_FILE = "./data/temp.pdf"
    INDEX_FILE = "./database/faiss.index"
    METADATA_FILE = "./database/metadata.pkl"
    USER_QUERY = "i am feeling depressed"

    if not GROQ_API_KEY:
        raise ValueError("❌ GROQ_API_KEY is not set in .env file.")

    if not (os.path.exists(INDEX_FILE) and os.path.exists(METADATA_FILE)):
        print("🔁 No FAISS index found. Creating new index from PDF...")
        build_index_from_pdf(PDF_FILE, INDEX_FILE, METADATA_FILE)
    else:
        print("📦 Using existing FAISS index and metadata.")

    answer = query_rag(USER_QUERY, GROQ_API_KEY, INDEX_FILE, METADATA_FILE)
    print("\n✅ Answer:\n", answer)
