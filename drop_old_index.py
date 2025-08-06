from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["aetherreg"]  
collection = db["obligations"]


collection.drop_indexes()
print("All indexes dropped successfully.")
