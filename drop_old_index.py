from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["aetherreg"]  # replace with your actual DB name
collection = db["obligations"]

# Drop all indexes (except _id)
collection.drop_indexes()
print("All indexes dropped successfully.")
