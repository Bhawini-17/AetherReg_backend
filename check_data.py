from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["aetherreg"]

async def check_obligations():
    cursor = db["obligations"].find()
    async for doc in cursor:
        print(doc)

asyncio.run(check_obligations())
