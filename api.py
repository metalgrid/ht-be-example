from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

users = []


@api.route("/users")
def list_users():
    return jsonify(users)


@api.route("/users/create")
def create_user():
    if request.is_json:
        # Get the JSON data from the request
        data = request.json

        # Process the data
        # For example, you can access specific keys in the data dictionary
        username = data.get("username")
        password = data.get("password")

        # Perform any processing here...

        users.append({"username": username, "password": password})

        # Return a JSON response
        response = {
            "message": f"User {username} created",
        }

        return jsonify(response), 200
    else:
        return jsonify({"error": "Invalid JSON"}), 400
