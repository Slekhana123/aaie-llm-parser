# LLM Similarity Check - Parser Testing & Validation

def validate_input(text):
    if not text:
        return {"status": "invalid", "reason": "empty input"}

    cleaned_input = text.strip()

    if not cleaned_input:
        return {"status": "invalid", "reason": "blank input"}

    if len(cleaned_input) < 5:
        return {"status": "invalid", "reason": "too short"}

    return {
        "status": "valid",
        "cleaned_input": cleaned_input,
        "message": "ready for similarity check"
    }


inputs = [
    "AI helps students learn better",
    "",
    "   ",
    "Hi"
]

for i in inputs:
    print("Input:", repr(i))
    print("Output:", validate_input(i))
    print("------")
