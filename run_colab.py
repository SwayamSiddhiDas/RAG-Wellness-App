# run_colab.py
from app.pipeline import build_pipeline

def main():
    pipeline = build_pipeline(kb_path="data/yoga_kb.txt")

    q1 = "What are the benefits of Surya Namaskar?"
    res1 = pipeline.ask(q1)
    print("Q:", q1)
    print("Safety:", res1["safety_flag"])
    print("Answer:", res1["answer"])
    print("-" * 60)

    q2 = "Can yoga cure depression?"
    res2 = pipeline.ask(q2)
    print("Q:", q2)
    print("Safety:", res2["safety_flag"])
    print("Answer:", res2["answer"])

if __name__ == "__main__":
    main()
