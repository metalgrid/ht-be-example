from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

users = [
    {
        "id": 1,
        "name": "Alice",
        "age": 20,
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 25,
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 30,
    },
]


@api.route("/users")
def list_users():
    return jsonify(users)


@api.route("/users/<int:id>")
def get_user(id):
    user = users.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)
