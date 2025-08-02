import asyncio
from database.obligation_repository import ObligationRepository
from obligation_extractor import extract_obligations_from_text
from vector_store import VectorStore
from obligation_schema import ObligationMetadata

# Replace with actual circular text
sample_text = """
RBI mandates that all banks must submit the KYC compliance report by 30th September 2025.
Failure to do so will attract a penalty under section 45 of the Banking Act.
"""

async def main():
    repo = ObligationRepository()
    vector_store = VectorStore()

    # Clear existing data (optional for testing)
    await repo.clear_all_obligations()

    obligations = extract_obligations_from_text(sample_text)

    if not obligations:
        print("❌ No obligations extracted.")
        return

    for obligation in obligations:
        inserted_id = await repo.save_obligation(obligation)
        print(f"✅ Saved obligation with ID: {inserted_id}")

    # Convert dicts to ObligationMetadata instances for indexing
    typed_obligations = obligations
    await vector_store.index_obligations(typed_obligations)
    print("📦 Obligations indexed and saved.")

if __name__ == "__main__":
    asyncio.run(main())
