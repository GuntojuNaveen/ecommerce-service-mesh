from flask import Flask, jsonify
import requests

app = Flask(__name__)

PRODUCT_SERVICE = "http://product-service:5000"
PAYMENT_SERVICE = "http://payment-service:5000"

@app.route("/orders")
def create_order():

    product_response = requests.get(
        f"{PRODUCT_SERVICE}/products"
    )

    payment_response = requests.get(
        f"{PAYMENT_SERVICE}/payment"
    )

    return jsonify({
        "order": "created",
        "product": product_response.json(),
        "payment": payment_response.json()
    })

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)
