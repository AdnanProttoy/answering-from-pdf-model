from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load the model once
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

def create_vector_store(chunks):
    """
    Convert text chunks to embeddings and create a FAISS vector store.
    """
    # Encode chunks to embeddings and convert to float32
    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, embeddings
