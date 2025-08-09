from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  
obligations_collection = []

@app.route("/")
def home():
    return "<h2>AetherReg Backend is Running</h2>"

@app.route("/api/obligations", methods=["GET"])
def get_obligations():
    obligations = list(obligations_collection)
    return jsonify(obligations)

@app.route("/api/dashboard", methods=["GET"])
def dashboard():
    return {
        "status": "success",
        "message": "Dashboard endpoint is working",
        "data": {
            "total_obligations": 5,
            "pending_obligations": 2
        }
    }

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"status": "error", "message": "No file selected"}), 400

    try:
        upload_folder = "uploads"
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)

        return jsonify({
            "status": "success",
            "message": "File uploaded successfully",
            "filename": file.filename,
            "path": file_path
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
