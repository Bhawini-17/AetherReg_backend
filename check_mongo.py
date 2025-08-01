import asyncio
from database.obligation_repository import ObligationRepository

async def check_data():
    repo = ObligationRepository()
    obligations = await repo.get_all_obligations()
    print(f"Total obligations in DB: {len(obligations)}")
    for i, ob in enumerate(obligations[:5], 1):  # Show only first 5
        print(f"\nObligation {i}:")
        print(ob)

if __name__ == "__main__":
    asyncio.run(check_data())
