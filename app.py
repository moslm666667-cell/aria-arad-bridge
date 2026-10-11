
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Aria-Arad Bridge API is running!"

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "ai_connected": False
    })

@app.post("/api/message")
def message():
    data = request.get_json(silent=True) or {}
    role = data.get("role", "")
    text = str(data.get("message", "")).strip()

    if role not in ("aria", "arad"):
        return jsonify({"error": "Invalid role"}), 400

    if not text:
        return jsonify({"error": "Empty message"}), 400

    if len(text) > 2000:
        return jsonify({"error": "Message too long"}), 400

    name = "آریا" if role == "aria" else "آراد"

    return jsonify({
        "role": role,
        "reply": f"{name} پیام را دریافت کرد: {text}",
        "mode": "demo"
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
