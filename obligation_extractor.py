from transformers import pipeline
import json
from obligation_schema import ObligationMetadata

# Load the model pipeline
nlp = pipeline("text-generation", model="tiiuae/falcon-rw-1b", tokenizer="tiiuae/falcon-rw-1b", max_new_tokens=256)

def extract_obligation_metadata(text: str) -> ObligationMetadata:
    prompt = f"""
Extract the following obligation metadata fields from the given text and return as JSON:
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

Example:

Text:
\"\"\"As per RBI/2023-24/45, regulated entities must update KYC data annually. Deadline: March 31. Non-compliance may attract penalty.\"\"\"

Output:
{{
  "obligation_text": "Regulated entities must update KYC data annually.",
  "issuer": "RBI",
  "circular_id": "RBI/2023-24/45",
  "effective_date": null,
  "frequency": "Annually",
  "action_required": "Update KYC data",
  "compliance_area": "KYC",
  "deadline": "March 31",
  "penalty": "Yes",
  "reference_clause": null
}}

Now extract from this text:

\"\"\"{text}\"\"\"

Return only the JSON.
"""

    try:
        response = nlp(prompt)[0]["generated_text"]
        json_start = response.find('{')
        json_str = response[json_start:]
        metadata_dict = json.loads(json_str)

        return ObligationMetadata(**metadata_dict)
    
    except Exception as e:
        print("Error extracting obligation metadata:", e)
        print("Raw model output:", response)
        return ObligationMetadata(
            obligation_text=text,
            issuer=None,
            circular_id=None,
            effective_date=None,
            frequency=None,
            action_required=None,
            compliance_area=None,
            deadline=None,
            penalty=None,
            reference_clause=None
        )
