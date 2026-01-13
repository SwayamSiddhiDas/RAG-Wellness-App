# app/generator.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.config import LOCAL_LLM_NAME

class LocalGenerator:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(LOCAL_LLM_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(LOCAL_LLM_NAME)

    def generate_answer(self, query: str, context_chunks: list[dict]) -> str:
        context_text = "\n\n".join([c["text"] for c in context_chunks])

        prompt = f"""
You are a wellness assistant specialized in yoga.
Answer ONLY using the context below.
If the answer is not found in the context, say:
"I do not have enough information from my knowledge base."

Context:
{context_text}

Question:
{query}

Answer:
"""

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        outputs = self.model.generate(**inputs, max_new_tokens=200)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
