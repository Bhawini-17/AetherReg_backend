from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["aetherreg"]
obligations_collection = db["obligations"]

# Home route (optional)
@app.route("/")
def home():
    return "<h2>AetherReg Backend is Running</h2>"

# Obligations API route
@app.route("/api/obligations")
def get_obligations():
    obligations = list(obligations_collection.find({}, {"_id": 0}))  # Exclude _id
    return jsonify(obligations)

if __name__ == "__main__":
    app.run(debug=True)
