def split_text(text, chunk_size=500, overlap=50):
    """
    Split the text into chunks of size `chunk_size` with optional `overlap`.
    """
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start = end - overlap  # move start by chunk_size - overlap

    return chunks
