# app.py
import os
import streamlit as st
from openai import OpenAI

from pdf_loader import load_pdf
from text_splitter import split_text
from embeddings import create_vector_store
from retriever import retrieve_chunks

# Initialize OpenAI client (make sure your API key is set in env variables)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Streamlit page setup
st.set_page_config(page_title="AI Document Agent")
st.title("Answering From pdf App Designed By PROTTOY")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Reading PDF..."):
        text = load_pdf(uploaded_file)
        chunks = split_text(text)
        index, embeddings = create_vector_store(chunks)
    st.success("PDF processed successfully!")

    # Ask question
    question = st.text_input("Ask a question from the document")

    if question:
        relevant_chunks = retrieve_chunks(question, chunks, index)
        context = "\n".join(relevant_chunks)

        prompt = f"""
        Answer the question using ONLY the context below.
        If the answer is not present, say "Not found in document."

        Context:
        {context}

        Question:
        {question}
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        st.subheader("Answer")
        st.write(response.choices[0].message.content)

    # Generate summary
    if st.button("Generate Summary"):
        prompt = f"""
        Create a professional summary using ONLY the content below.

        Content:
        {text}
        """

        summary_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        st.subheader("Summary")
        st.write(summary_response.choices[0].message.content)
