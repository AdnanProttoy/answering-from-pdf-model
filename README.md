# Answering From PDF – AI Document Agent

A **Streamlit-based AI application** that allows users to upload PDF documents and ask questions based on the content of those PDFs.  
The app extracts text from PDFs, splits it into chunks, stores embeddings in a vector database (FAISS), and retrieves relevant context to generate accurate answers using the OpenAI API.

 **Live Demo (Streamlit Cloud):** https://your-app-url.streamlit.app  
 **GitHub Repository:** https://github.com/AdnanProttoy/answering-from-pdf-model

---

## Features

1. Upload PDF documents  
2. Extract text from PDFs  
3. Split text into semantic chunks  
4. Vector-based semantic search using FAISS  
5. Question answering using OpenAI API  
6. Fast and interactive UI with Streamlit  
7. Deployed on Streamlit Cloud  

##  Tech Stack

- Python  
- Streamlit  
- OpenAI API  
- FAISS (Vector Database)  
- Sentence Transformers  
- PyPDF2  
- NumPy  


##  Project Structure

```text
answering-from-pdf-model/
│
├── app.py                 # Main Streamlit application
├── pdf_loader.py          # PDF text extraction logic
├── text_splitter.py       # Text chunking logic
├── vector_store.py        # FAISS vector store creation
├── retriever.py           # Semantic retrieval logic
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignored files and folders

## Run the Project Locally

1.Clone the Repository
```bash
git clone https://github.com/AdnanProttoy/answering-from-pdf-model.git
cd answering-from-pdf-model

2.Create & Activate Virtual Environment
   python -m venv venv
  # macOS / Linux
  source venv/bin/activate
  # Windows
  venv\Scripts\activate

3.Install Dependencies
  pip install -r requirements.txt

4.Set Environment Variable (OpenAI API Key)
  export OPENAI_API_KEY="your_openai_api_key"
5.Windows (PowerShell)
  setx OPENAI_API_KEY "your_openai_api_key"

6.Run the app
  streamlit run app.py
