from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

<<<<<<< HEAD
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_vector_store(chunks):
    embeddings = model.encode(chunks, convert_to_numpy=True)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
=======
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(chunks):
    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

>>>>>>> 546c7af (Add .gitignore and remove venv)
    return index, embeddings
