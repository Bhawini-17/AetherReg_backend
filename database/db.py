from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = "aetherreg"

client = AsyncIOMotorClient(MONGODB_URI)
db = client[MONGO_DB_NAME]
