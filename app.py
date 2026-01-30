# ===============================
# STEP 1: Load documents
# ===============================
with open("data.txt", "r") as f:
    documents = [line.strip() for line in f if line.strip()]

# ===============================
# STEP 2: Load embedding model
# ===============================
from sentence_transformers import SentenceTransformer
import torch
from torch.nn.functional import normalize

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# ===============================
# STEP 3: Create document embeddings
# ===============================
doc_embeddings = embed_model.encode(documents, convert_to_tensor=True)
doc_embeddings = normalize(doc_embeddings, p=2, dim=1)

# ===============================
# STEP 4: Import OpenAI client
# ===============================
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ===============================
# STEP 5: Question loop
# ===============================
while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        print("Goodbye!")
        break

    # ===============================
    # STEP 6: Embed query
    # ===============================
    query_embedding = embed_model.encode([query], convert_to_tensor=True)
    query_embedding = normalize(query_embedding, p=2, dim=1)

    # ===============================
    # STEP 7: Similarity search (Top-K)
    # ===============================
    from torch.nn.functional import cosine_similarity

    scores = cosine_similarity(query_embedding, doc_embeddings).squeeze(0)

    top_k = 3
    top_scores, top_indices = torch.topk(scores, k=top_k)

    # ===============================
    # STEP 8: Apply threshold
    # ===============================
    threshold = 0.3
    retrieved_docs = []

    for idx, score in zip(top_indices, top_scores):
        if score >= threshold:
            retrieved_docs.append(documents[idx])

    if not retrieved_docs:
        print("\nAnswer not found in documents.")
        continue

    retrieved_context = "\n".join(retrieved_docs)

    # ===============================
    # STEP 9: Build strict prompt
    # ===============================
    prompt = f"""
You are a strict assistant.

Answer ONLY from the context below.
If the answer is not present, say:
"I don't know based on the provided documents."

Context:
{retrieved_context}

Question:
{query}

Answer (max 3 sentences):
"""

    # ===============================
    # STEP 10: Call OpenAI
    # ===============================
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content

    # ===============================
    # STEP 11: Print answer
    # ===============================
    print("\n===== ANSWER =====")
    print(answer)

