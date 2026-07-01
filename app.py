from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

notes = [
    {
        "message": "hey baby i love you so much",
        "date": "Sunday, 10 May 2026",
        "time": "01:00"
    }
]

current_note = {"message": "hey baby i love you so much", "updated": False}

@app.route("/")
def index():
    return send_from_directory('.', 'display.html')

@app.route("/display")
def display():
    return send_from_directory('.', 'display.html')

@app.route("/send")
def send_page():
    return send_from_directory('.', 'send.html')

@app.route("/note", methods=["GET"])
def get_note():
    return jsonify(current_note)

@app.route("/note", methods=["POST"])
def set_note():
    data = request.get_json()
    msg = data["message"]
    current_note["message"] = msg
    current_note["updated"] = True
    notes.append({
        "message": msg,
        "date": datetime.now().strftime("%A, %-d %B %Y"),
        "time": datetime.now().strftime("%H:%M")
    })

    print(notes[-1]["date"])
    return jsonify({"status": "ok"})

@app.route("/history", methods=["GET"])
def history():
    print("fetch")
    return jsonify(list(reversed(notes)))

@app.route("/ack", methods=["POST"])
def ack():
    current_note["updated"] = False
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)