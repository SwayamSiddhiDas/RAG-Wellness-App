# app/safety.py
HIGH_RISK_KEYWORDS = [
    "cure", "diagnose", "treatment", "medicine", "medication",
    "depression", "anxiety", "panic", "suicidal",
    "injury", "fracture", "pain", "surgery", "dose"
]

def classify_query(query: str) -> str:
    q = query.lower()
    for w in HIGH_RISK_KEYWORDS:
        if w in q:
            return "UNSAFE"
    return "SAFE"

def safety_response(flag: str) -> str | None:
    if flag == "UNSAFE":
        return (
            "I’m not a medical professional, so I can’t provide medical advice or diagnosis. "
            "Please consult a qualified healthcare professional. "
            "If this feels urgent or serious, seek help immediately."
        )
    return None
