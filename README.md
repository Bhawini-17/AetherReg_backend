# AetherReg_backend
# 📘 AetherReg – AI-Powered Compliance Intelligence

AetherReg is a compliance automation tool that reads regulatory circulars (PDFs), extracts obligations, assigns tasks using AI agents, and integrates with Slack and other systems to ensure timely compliance.

---

## 🚀 Features

- 🧠 OCR for scanned & native PDFs
- 🔍 NLP-based obligation extraction (BERT)
- 🗃️ MongoDB storage
- 🤖 Task assignment via LangChain agent
- 📨 Slack integration
- 🌐 API-based frontend-ready backend

---

## 🛠 Tech Stack

- Python (Flask)
- MongoDB
- FAISS (Embeddings & Search)
- HuggingFace Transformers
- Tesseract OCR
- LangChain
- Slack Webhooks

---

## 🧾 API Routes

| Method | Endpoint              | Description                      |
|--------|-----------------------|----------------------------------|
| POST   | `/upload`             | Upload a new circular PDF        |
| GET    | `/api/obligations`    | Get all extracted obligations    |
| GET    | `/`                   | Simple HTML UI fallback          |

---

## 🖥️ How to Run Locally

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd aetherreg
