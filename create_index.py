from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["aetherreg"]

async def create_index():
    await db["obligations"].create_index([
        ("obligation_text", "text"),
        ("issuer", "text"),
        ("circular_id", "text"),
        ("action_required", "text"),
        ("compliance_area", "text")
    ])
    print("✅ Text index created.")

asyncio.run(create_index())
