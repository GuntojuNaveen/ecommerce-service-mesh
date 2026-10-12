from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Naveen"
    }
]

@app.route("/users")
def get_users():
    return jsonify(users)

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)
