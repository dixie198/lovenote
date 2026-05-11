from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

note = {"message": "I love you ❤️", "updated": False}

@app.route("/note", methods=["GET"])
def get_note():
    return jsonify(note)

@app.route("/note", methods=["POST"])
def set_note():
    data = request.get_json()
    note["message"] = data["message"]
    note["updated"] = True
    return jsonify({"status": "ok"})

@app.route("/ack", methods=["POST"])
def ack():
    note["updated"] = False
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)