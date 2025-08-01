# RAG System - PDF to Q&A with Groq

A simple RAG (Retrieval-Augmented Generation) system that extracts text from PDFs, builds a FAISS index, and answers questions using Groq's Llama model.

## 🚀 Features

- **PDF Text Extraction**: Extract text from PDF documents
- **Semantic Search**: FAISS index for fast document retrieval
- **Intelligent Q&A**: Groq's Llama 3 8B model for answer generation
- **Simple Workflow**: One script handles everything

## 📋 Requirements

- Python 3.8+
- Groq API key
- PDF file to process

## 🛠️ Installation

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Set up environment variables**:
```bash
# Create .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

3. **Place your PDF file**:
```bash
# Put your PDF in the data folder
cp your_document.pdf ./data/temp.pdf
```

## 🎯 Usage

### Quick Start

1. **Run the script**:
```bash
python main.py
```

2. **The script will**:
   - Extract text from `./data/temp.pdf`
   - Build FAISS index (if not exists)
   - Answer the default question: "i am feeling depressed"

### Custom Usage

```python
from main import build_index_from_pdf, query_rag

# Build index from PDF
build_index_from_pdf(
    pdf_path="./data/your_document.pdf",
    index_path="./database/faiss.index",
    metadata_path="./database/metadata.pkl"
)

# Query the system
answer = query_rag(
    query="Your question here",
    groq_api_key="your_api_key",
    index_path="./database/faiss.index",
    metadata_path="./database/metadata.pkl"
)
print(answer)
```

## 📁 Project Structure

```
RAG_without_framework/
├── main.py                 # Main RAG implementation
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── data/
│   └── temp.pdf          # Your PDF document
└── database/
    ├── faiss.index       # FAISS vector index
    └── metadata.pkl      # Document chunks metadata
```

## 🔧 How It Works

1. **PDF Processing**: Extracts text from PDF using PyPDF2
2. **Text Chunking**: Splits text into 300-word chunks
3. **Embedding**: Uses Sentence Transformers to create embeddings
4. **Indexing**: Builds FAISS index for fast similarity search
5. **Retrieval**: Finds most relevant chunks for a question
6. **Generation**: Uses Groq's Llama model to generate answers

## 📊 Configuration

- **Embedding Model**: `all-MiniLM-L6-v2`
- **LLM Model**: `llama3-8b-8192` (Groq)
- **Chunk Size**: 300 words
- **Top-k Retrieval**: 3 chunks
- **Temperature**: 0.7

## 🚨 Troubleshooting

1. **GROQ_API_KEY not set**: Add your API key to `.env` file
2. **PDF not found**: Place your PDF in `./data/temp.pdf`
3. **Import errors**: Install dependencies with `pip install -r requirements.txt`

## 📝 Example Output

```
📄 Reading PDF...
✂️ Chunking...
🔍 Embedding and building index...
✅ FAISS index and metadata saved.
📦 Using existing FAISS index and metadata.
🧾 Full Response from Groq:
{...}
✅ Answer:
Based on the context provided, here's the answer to your question...
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests! 