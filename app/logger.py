import json
from datetime import datetime
from app.config import LOG_FILE

def log_interaction(query, retrieved_chunks, answer, safety_flag, latency_ms):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "query": query,
        "retrieved_chunks": retrieved_chunks,
        "answer": answer,
        "safety_flag": safety_flag,
        "latency_ms": latency_ms
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
