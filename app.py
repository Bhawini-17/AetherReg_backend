from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["aetherreg"]
circulars_collection = db["circulars"]
obligations_collection = db["obligations"]

@app.route("/")
def index():
    circulars = list(circulars_collection.find())
    return render_template("index.html", circulars=circulars)

@app.route("/api/dashboard", methods=["GET"])
def dashboard():
    total = obligations_collection.count_documents({})
    completed = obligations_collection.count_documents({"status": "completed"})
    pending = obligations_collection.count_documents({"status": "pending"})

    today = datetime.today()
    upcoming_deadline = today + timedelta(days=7)
    upcoming = obligations_collection.count_documents({
        "deadline": {
            "$gte": today,
            "$lte": upcoming_deadline
        },
        "status": "pending"
    })

    return jsonify({
        "total_obligations": total,
        "completed_obligations": completed,
        "pending_obligations": pending,
        "upcoming_deadlines": upcoming
    })

if __name__ == "__main__":
    app.run(debug=True)
