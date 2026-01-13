# NextYou – “Ask Me Anything” Wellness RAG Micro-App (Colab-First, No External Keys)

This project implements a **Retrieval-Augmented Generation (RAG)** based wellness/yoga assistant titled **“Ask Me Anything”**.

✅ **No OpenAI API key required**  
✅ **No MongoDB URI required** (local JSONL logging instead)  
✅ **Colab-first** and reproducible  
✅ Full pipeline: **chunking → embeddings → FAISS retrieval → local LLM generation**  
✅ Includes **backend safety logic** for health-related/sensitive queries  
✅ Logs **user query, retrieved context, response, safety flag, latency**

---

## 1) Features (Assignment Checklist)

### ✅ Structured wellness / yoga knowledge base
- Uses a text-based structured KB (included as `data/yoga_kb.txt`)
- Chunked into overlapping segments for better retrieval

### ✅ Complete RAG Pipeline
- Chunking + overlap
- Embeddings using `sentence-transformers`
- Vector retrieval using **FAISS**
- Context injection into local LLM prompt

### ✅ Backend Safety Logic
- Keyword + rule-based safety classification:
  - `SAFE`
  - `UNSAFE` (medical/treatment/diagnosis requests)
- Unsafe queries return a refusal + guidance to consult professionals

### ✅ Logging (Auditability)
- Writes structured logs to `logs.jsonl` (1 JSON per line):
  - query
  - retrieved chunks (IDs + text + source)
  - final answer
  - safety flag
  - latency

---

## 2) Repo Structure

```
nextyou-wellness-rag/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── safety.py
│   ├── logger.py
│   ├── chunking.py
│   ├── embeddings_store.py
│   ├── generator.py
│   └── pipeline.py
│
├── data/
│   └── yoga_kb.txt
│
├── run_colab.py
├── requirements.txt
└── README.md
```

---

## 3) Quickstart (Google Colab)

### Step 1 — Upload the knowledge base
Upload `data/yoga_kb.txt` or your own `yoga_kb.txt`.

### Step 2 — Install requirements
In Colab:
```bash
!pip install -r requirements.txt
```

### Step 3 — Run the pipeline
```python
from app.pipeline import build_pipeline

pipeline = build_pipeline(kb_path="yoga_kb.txt")  # or "data/yoga_kb.txt"
result = pipeline.ask("What are the benefits of Surya Namaskar?")
print(result["safety_flag"])
print(result["answer"])
```

### Step 4 — Check logs
```bash
!tail -n 5 logs.jsonl
```

---

## 4) Run Locally (Optional)

> This project was designed for Colab, but runs locally too.

```bash
pip install -r requirements.txt
python run_colab.py
```

---

## 5) Notes on Design Choices

### Why FAISS?
- Lightweight and fast vector similarity search
- Works offline and is easy to reproduce in Colab

### Why FLAN-T5-Large?
- Runs without external API keys
- Lightweight enough for Colab CPU/GPU
- Good for instruction-style answering in constrained domains

### Why JSONL logging instead of MongoDB?
- Keeps project runnable without credentials
- Preserves auditability (required by assignment)
- Can be swapped with MongoDB easily later

---

## 6) Safety Disclaimer

This assistant provides **general wellness information** only.  
It does **not** provide medical diagnosis or treatment advice.

If a user asks for medical help, the system will refuse and recommend consulting a qualified healthcare professional.

---

## 7) Example Queries

✅ Safe:
- “What are the benefits of Surya Namaskar?”
- “How do I do Child’s Pose?”
- “What is Nadi Shodhana?”

🚫 Unsafe:
- “Can yoga cure depression?”
- “Which pose will heal my injury?”
- “Should I stop medicine if I do yoga?”

---

## 8) License
MIT (you can change this if needed)
