from obligation_extractor import extract_obligation_metadata

# Simulated PDF text for demo
sample_text = """
The bank shall maintain a CRR of 4.5% at all times.
It is mandatory for all scheduled banks to file STRs within 7 days.
Every entity should conduct quarterly audits of KYC compliance.
"""

results = extract_obligation_metadata(sample_text)

for i, item in enumerate(results, 1):
    print(f"\nObligation {i}:")
    print(item.model_dump_json(indent=2))
