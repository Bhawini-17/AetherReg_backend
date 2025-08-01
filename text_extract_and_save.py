import asyncio
from obligation_extractor import extract_obligations_from_text
from database.obligation_repository import ObligationRepository

sample_text = """
All regulated entities must submit quarterly compliance reports to the RBI by the 10th of the following month. 
Non-submission will attract a penalty of ₹5,000 per day. This applies to all NBFCs under circular RBI/2024-25/101, effective from April 1st, 2025.
"""

async def run():
    repo = ObligationRepository()
    obligations = extract_obligations_from_text(sample_text)
    
    if not obligations: 
        print("❌ No obligations extracted.")
        return
    
    for obligation in obligations:
        inserted_id = await repo.save_obligation(obligation)
        print(f"✅ Saved obligation with ID: {inserted_id}")

if __name__ == "__main__":
    asyncio.run(run())
