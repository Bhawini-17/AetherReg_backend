from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["aetherreg"]
obligations_collection = db["obligations"]

# Home route
@app.route("/")
def home():
    return "<h2>AetherReg Backend is Running</h2>"

# Obligations route
@app.route("/api/obligations", methods=["GET"])
def get_obligations():
    obligations = list(obligations_collection.find({}, {"_id": 0}))
    return jsonify(obligations)

# ✅ File upload route
@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    return jsonify({"message": "File uploaded", "filename": file.filename})

if __name__ == "__main__":
    app.run(debug=True)
