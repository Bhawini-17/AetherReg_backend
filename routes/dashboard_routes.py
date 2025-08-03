# aetherreg/routes/dashboard_routes.py

from flask import Blueprint, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta

dashboard_bp = Blueprint('dashboard', __name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["aetherreg"]
obligations = db["obligations"]

@dashboard_bp.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    total = obligations.count_documents({})
    completed = obligations.count_documents({"status": "completed"})
    pending = obligations.count_documents({"status": "pending"})

    today = datetime.today()
    upcoming_deadline = today + timedelta(days=7)
    upcoming = obligations.count_documents({
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
