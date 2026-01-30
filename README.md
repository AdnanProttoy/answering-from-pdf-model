# RAG Document Question Answering (QA) App

This project demonstrates a **Retrieval-Augmented Generation (RAG)** system using Python.  
It can answer questions based on a set of provided documents using **semantic search + OpenAI GPT-3.5**.


Features

- Embeds documents using `SentenceTransformer` (`all-MiniLM-L6-v2`)  
- Retrieves relevant context using **cosine similarity**  
- Generates answers using **OpenAI GPT-3.5-turbo**  
- Strict prompt ensures answers come **only from the provided documents**  
- Easy to add your own documents in `data.txt`
 Installation

1. Clone the repository:
```bash
git clone https://github.com/AdnanProttoy/rag-document-qa.git
cd rag-document-qa
