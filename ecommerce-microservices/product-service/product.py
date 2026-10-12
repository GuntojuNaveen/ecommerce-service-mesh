from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 75000
    },
    {
        "id": 2,
        "name": "Headphones",
        "price": 3000
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 1500
    }
]

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)
