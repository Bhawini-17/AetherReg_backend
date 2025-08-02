from pymongo import MongoClient

# Connect to your local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["aetherreg"]
collection = db["obligations"]

# Create a text index on the 'obligation_text' field
collection.create_index([("obligation_text", "text")])

print("✅ Text index created successfully.")
