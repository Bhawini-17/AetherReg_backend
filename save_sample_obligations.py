import asyncio
from database.obligation_repository import ObligationRepository
from obligation_extractor import extract_obligations_from_text

# Replace with actual circular text
sample_text = """
RBI mandates that all banks must submit the KYC compliance report by 30th September 2025.
Failure to do so will attract a penalty under section 45 of the Banking Act.
"""

async def main():
    repo = ObligationRepository()
    obligations = extract_obligations_from_text(sample_text)

    if not obligations:
        print("❌ No obligations extracted.")
        return

    for obligation in obligations:
        inserted_id = await repo.save_obligation(obligation)
        print(f"✅ Saved obligation with ID: {inserted_id}")

if __name__ == "__main__":
    asyncio.run(main())
