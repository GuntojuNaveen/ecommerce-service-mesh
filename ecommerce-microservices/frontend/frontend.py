from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://user-service:5000"
PRODUCT_SERVICE = "http://product-service:5000"
ORDER_SERVICE = "http://order-service:5000"

@app.route("/")
def home():

    users = requests.get(
        f"{USER_SERVICE}/users"
    ).json()

    products = requests.get(
        f"{PRODUCT_SERVICE}/products"
    ).json()

    return jsonify({
        "application": "E-Commerce Application",
        "users": users,
        "products": products
    })

@app.route("/order")
def order():

    response = requests.get(
        f"{ORDER_SERVICE}/orders"
    )

    return jsonify(response.json())

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)
