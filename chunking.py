# app/chunking.py
from app.config import CHUNK_SIZE_WORDS, CHUNK_OVERLAP_WORDS

def chunk_text(text: str, chunk_size: int = CHUNK_SIZE_WORDS, overlap: int = CHUNK_OVERLAP_WORDS):
    words = text.split()
    chunks = []
    i = 0

    while i < len(words):
        chunk_words = words[i:i + chunk_size]
        chunks.append(" ".join(chunk_words))
        i += max(1, chunk_size - overlap)

    return chunks
