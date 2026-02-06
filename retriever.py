import numpy as np
from sentence_transformers import SentenceTransformer

# Load the model once globally
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(question, chunks, index, top_k=3):
    """
    Retrieve the most relevant text chunks from an index given a question.
    """
    # Encode the question
    query_embedding = model.encode([question])
    query_embedding = np.array(query_embedding).astype("float32")

    # Search in the vector index
    distances, indices = index.search(query_embedding, top_k)

    # Return the top relevant chunks
    results = [chunks[i] for i in indices[0]]
    return results
