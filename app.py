with open("data.txt", "r") as f:
    documents = [line.strip() for line in f if line.strip()]

from sentence_transformers import SentenceTransformer
import torch
from torch.nn.functional import normalize

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embed_model.encode(documents, convert_to_tensor=True)
doc_embeddings = normalize(doc_embeddings, p=2, dim=1)

import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        print("Goodbye!")
        break

    query_embedding = embed_model.encode([query], convert_to_tensor=True)
    query_embedding = normalize(query_embedding, p=2, dim=1)

    from torch.nn.functional import cosine_similarity
    scores = cosine_similarity(query_embedding, doc_embeddings).squeeze(0)

    top_k = min(3, len(documents))
    top_scores, top_indices = torch.topk(scores, k=top_k)

    threshold = 0.3
    retrieved_docs = [
        documents[idx] for idx, score in zip(top_indices, top_scores) if score >= threshold
    ]

    if not retrieved_docs:
        print("\nAnswer not found in documents.")
        continue

    retrieved_context = "\n".join(retrieved_docs)

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

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    answer = response.choices[0].message.content
    print("ANSWER")
    print(answer)


