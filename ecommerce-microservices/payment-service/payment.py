from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/payment")
def payment():
    return jsonify({
        "status": "success",
        "message": "Payment processed successfully"
    })

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)
