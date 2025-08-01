import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from obligation_schema import ObligationMetadata
import json
import re

# Load model and tokenizer (CPU)
device = torch.device("cpu")
model_name = "MBZUAI/LaMini-T5-738M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

def extract_obligations_from_text(text: str) -> list[ObligationMetadata]:
    prompt = f"""
Extract the following obligation metadata fields from the given text and return as JSON list:
1. obligation_text
2. issuer
3. circular_id
4. effective_date
5. frequency
6. action_required
7. compliance_area
8. deadline
9. penalty
10. reference_clause

Text:
\"\"\"{text}\"\"\"

Output:
"""
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=512)
    raw_output = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Try JSON parse
    try:
        json_start = raw_output.find("{")
        if json_start == -1:
            raise ValueError("No JSON found")

        json_str = raw_output[json_start:]
        data = json.loads(json_str)

        if isinstance(data, dict):
            data = [data]

        return [ObligationMetadata(**item) for item in data]

    except Exception as e:
        print("❌ Error extracting obligation metadata:", e)
        print("Raw model output:\n", raw_output)

        # Attempt regex fallback
        fields = {
            "obligation_text": r"obligation_text[:\-–]\s*\"?([^\"]+)\"?",
            "issuer": r"Issuer[:\-–]\s*\"?([^\"]+)\"?",
            "circular_id": r"Circular_id[:\-–]\s*\"?([^\"]+)\"?",
            "effective_date": r"Effective date[:\-–]\s*\"?([^\"]+)\"?",
            "frequency": r"Frequency[:\-–]\s*\"?([^\"]+)\"?",
            "action_required": r"Action_required[:\-–]\s*\"?([^\"]+)\"?",
            "compliance_area": r"Compliance area[:\-–]\s*\"?([^\"]+)\"?",
            "deadline": r"Deadline[:\-–]\s*\"?([^\"]+)\"?",
            "penalty": r"Penalty[:\-–]\s*\"?([^\"]+)\"?",
            "reference_clause": r"Reference_clause[:\-–]\s*\"?([^\"]+)\"?",
        }

        extracted = {}
        for key, pattern in fields.items():
            match = re.search(pattern, raw_output, re.IGNORECASE)
            if match:
                extracted[key] = match.group(1).strip()

        if "obligation_text" in extracted:
            return [ObligationMetadata(**extracted)]

        return []
