from database.db import db
from obligation_schema import ObligationMetadata

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
            results.append(doc)
        return results
