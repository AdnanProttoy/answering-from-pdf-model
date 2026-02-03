<<<<<<< HEAD
import numpy as np

def retrieve_chunks(question, chunks, index, embeddings, top_k=3):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([question])
    D, I = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in I[0]]
=======
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(question, chunks, index, k=3):
    q_embedding = model.encode([question])
    q_embedding = np.array(q_embedding).astype("float32")

    distances, indices = index.search(q_embedding, k)

    results = [chunks[i] for i in indices[0]]
    return results
>>>>>>> 546c7af (Add .gitignore and remove venv)
