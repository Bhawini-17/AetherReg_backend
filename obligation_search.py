import asyncio
from database.obligation_repository import ObligationRepository
from obligation_schema import ObligationMetadata

async def search_obligations(query: str):
    repo = ObligationRepository()
    results = await repo.search_obligations(query)
    return results

async def search_loop():
    query = input(" Enter search query: ").strip()
    if not query:
        print(" Please enter a valid search query.")
        return

    results = await search_obligations(query)

    if not results:
        print(" No obligations found.")
        return

    print(f"\nFound {len(results)} obligation(s):\n")

    for ob in results:
        print(f"\n- {ob.obligation_text}")
        print(f"  Issuer: {ob.issuer}")
        print(f"  Circular Id: {ob.circular_id}")
        print(f"  Effective Date: {ob.effective_date}")
        print(f"  Frequency: {ob.frequency}")
        print(f"  Action Required: {ob.action_required}")
        print(f"  Compliance Area: {ob.compliance_area}")
        print(f"  Deadline: {ob.deadline}")
        print(f"  Penalty: {ob.penalty}")
        print(f"  Reference Clause: {ob.reference_clause}")
        print("------")

if __name__ == "__main__":
    asyncio.run(search_loop())
