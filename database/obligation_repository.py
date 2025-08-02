from motor.motor_asyncio import AsyncIOMotorClient
from obligation_schema import ObligationMetadata
from typing import List

# MongoDB setup
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["aetherreg"]

class ObligationRepository:
    def __init__(self):
        self.collection = db["obligations"]

    async def save_obligation(self, metadata: ObligationMetadata):
        doc = metadata.model_dump()
        result = await self.collection.insert_one(doc)
        return str(result.inserted_id)

    async def get_all_obligations(self):
        cursor = self.collection.find({})
        results = []
        async for doc in cursor:
            results.append(ObligationMetadata(**doc))
        return results

    async def search_obligations(self, query: str) -> List[ObligationMetadata]:
        cursor = self.collection.find({
            "$text": {"$search": query}
        })
        results = []
        async for doc in cursor:
            results.append(ObligationMetadata(**doc))
        return results
