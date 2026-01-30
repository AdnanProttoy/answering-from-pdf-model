# rag-document-qa

# Document-based Question Answering with GPT

This project demonstrates a **retrieval-augmented generation (RAG)** system using **SentenceTransformers** and **OpenAI GPT-3.5**.  
It answers user questions based on a custom dataset (`data.txt`).

## Features

Loads a custom dataset of text documents.
Computes embeddings using `SentenceTransformer` for semantic search.
Retrieves relevant documents based on cosine similarity.
Generates answers using GPT-3.5 **only from the retrieved documents**.
Strict prompt ensures GPT only uses provided context.
Handles multiple questions interactively.


