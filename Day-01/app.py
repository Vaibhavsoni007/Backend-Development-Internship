from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
items = []


@app.route("/")
def home():
    return "Welcome to Day-01 Flask Backend API!"


# GET all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


# POST a new item
@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()

    items.append(data)

    return jsonify({
        "message": "Item added successfully",
        "item": data
    }), 201


if __name__ == "__main__":
    app.run(debug=True)