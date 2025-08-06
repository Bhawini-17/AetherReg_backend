from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["aetherreg"]
collection = db["obligations"]

collection.create_index([("obligation_text", "text")])

print("Text index created successfully.")
