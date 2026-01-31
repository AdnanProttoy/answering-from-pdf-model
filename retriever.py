import numpy as np

def retrieve_chunks(question, chunks, index, embeddings, top_k=3):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([question])
    D, I = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in I[0]]
