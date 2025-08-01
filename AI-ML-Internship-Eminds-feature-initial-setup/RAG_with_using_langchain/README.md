# RAG with LangChain

A simple PDF chatbot application that uses Retrieval-Augmented Generation (RAG) with LangChain framework to answer questions about uploaded PDF documents.

## Features

- 📄 Upload and process PDF files
- 🤖 Chat with your PDF documents using Groq LLM
- 🔍 Semantic search using FAISS vector database
- 💬 Interactive Streamlit web interface

## Project Structure

```
RAG_with_using_langchain/
├── rag_proj/
│   ├── chatpdf1.py      # Main application file
│   └── requirements.txt  # Python dependencies
└── README.md            # This file
```

## Prerequisites

- Python 3.8 or higher
- Groq API key (get it from [Groq Console](https://console.groq.com/))

## Installation

1. Navigate to the project directory:
   ```bash
   cd rag_proj
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the `rag_proj` directory
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run chatpdf1.py
   ```

2. Open your web browser and go to the URL shown in the terminal (usually `http://localhost:8501`)

3. Upload a PDF file using the file uploader

4. Ask questions about the PDF content in the text input field

5. Get AI-powered answers based on the PDF content

## How It Works

1. **PDF Processing**: Extracts text from uploaded PDF files
2. **Text Chunking**: Splits text into smaller chunks for better processing
3. **Embedding Generation**: Creates vector embeddings using sentence-transformers
4. **Vector Storage**: Stores embeddings in FAISS for fast similarity search
5. **Question Answering**: Uses Groq LLM to generate answers based on relevant context
6. **Web Interface**: Provides an intuitive Streamlit interface for interaction

## Dependencies

- `streamlit` - Web application framework
- `langchain` - LLM framework
- `langchain-community` - Community integrations
- `langchain-groq` - Groq LLM integration
- `faiss-cpu` - Vector similarity search
- `PyPDF2` - PDF text extraction
- `python-dotenv` - Environment variable management
- `sentence-transformers` - Text embeddings

## Technologies Used

- **LangChain**: LLM orchestration framework
- **Groq**: Fast LLM inference
- **FAISS**: Vector similarity search
- **Streamlit**: Web application interface
- **Sentence Transformers**: Text embeddings
- **PyPDF2**: PDF processing

## Note

Make sure you have a valid Groq API key and sufficient credits to use the service. The application uses the `llama3-8b-8192` model for generating responses. 