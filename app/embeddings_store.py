
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL_NAME

class EmbeddingStore:
    def __init__(self):
        self.embed_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        self.dimension = 384  # for all-MiniLM-L6-v2
        self.index = faiss.IndexFlatL2(self.dimension)
        self.documents = []

    def add_documents(self, docs: list[dict]):
        texts = [d["text"] for d in docs]
        embeddings = self.embed_model.encode(texts, show_progress_bar=True)
        self.index.add(np.array(embeddings).astype("float32"))
        self.documents.extend(docs)

    def retrieve(self, query: str, k: int = 4) -> list[dict]:
        query_embedding = self.embed_model.encode([query])
        _, indices = self.index.search(np.array(query_embedding).astype("float32"), k)

        results = []
        for idx in indices[0]:
            if 0 <= idx < len(self.documents):
                results.append(self.documents[idx])
        return results
