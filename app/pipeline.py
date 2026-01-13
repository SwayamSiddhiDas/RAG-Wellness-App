
import time
from app.chunking import chunk_text
from app.embeddings_store import EmbeddingStore
from app.generator import LocalGenerator
from app.safety import classify_query, safety_response
from app.logger import log_interaction
from app.config import TOP_K

class WellnessRAGPipeline:
    def __init__(self, store: EmbeddingStore, generator: LocalGenerator, top_k: int = TOP_K):
        self.store = store
        self.generator = generator
        self.top_k = top_k

    def ask(self, query: str) -> dict:
        start = time.time()

        safety_flag = classify_query(query)
        safe_reply = safety_response(safety_flag)

        retrieved_chunks = []
        if safe_reply:
            answer = safe_reply
        else:
            retrieved_chunks = self.store.retrieve(query, k=self.top_k)
            answer = self.generator.generate_answer(query, retrieved_chunks)

        latency_ms = int((time.time() - start) * 1000)

        log_interaction(
            query=query,
            retrieved_chunks=retrieved_chunks,
            answer=answer,
            safety_flag=safety_flag,
            latency_ms=latency_ms
        )

        return {
            "query": query,
            "safety_flag": safety_flag,
            "retrieved_chunks": retrieved_chunks,
            "answer": answer,
            "latency_ms": latency_ms
        }

def build_pipeline(kb_path: str = "data/yoga_kb.txt") -> WellnessRAGPipeline:
    # Read KB
    with open(kb_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Chunk KB
    chunks = chunk_text(raw_text)

    docs = [
        {"chunk_id": f"KB_{i}", "text": chunk, "source": kb_path}
        for i, chunk in enumerate(chunks)
    ]

    # Build store + generator
    store = EmbeddingStore()
    store.add_documents(docs)

    generator = LocalGenerator()

    return WellnessRAGPipeline(store=store, generator=generator)
