import asyncio
from database.obligation_repository import ObligationRepository

async def main():
    repo = ObligationRepository()
    obligations = await repo.get_all_obligations()

    print("\n--- All obligations in DB ---")
    for doc in obligations:
        print(doc)

if __name__ == "__main__":
    asyncio.run(main())
