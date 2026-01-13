# app/config.py
LOG_FILE = "logs.jsonl"

# Embedding model
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# Local LLM (no API keys)
LOCAL_LLM_NAME = "google/flan-t5-large"

# Chunking settings
CHUNK_SIZE_WORDS = 400
CHUNK_OVERLAP_WORDS = 80

# Retrieval
TOP_K = 4
