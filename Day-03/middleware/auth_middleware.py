import jwt
from functools import wraps
from flask import request, jsonify, current_app


def token_required(function):

    @wraps(function)
    def decorated(*args, **kwargs):

        token = None

        # Get token from Authorization header
        if "Authorization" in request.headers:

            auth_header = request.headers["Authorization"]

            # Expected format:
            # Bearer JWT_TOKEN
            token = auth_header.split(" ")[1]


        # Token missing
        if not token:

            return jsonify({
                "message": "Token is missing"
            }), 401


        try:
            # Verify token
            data = jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )

            print("Logged in User ID:", data["user_id"])

        except Exception as error:

            return jsonify({
                "message": "Invalid or expired token"
            }), 401


        return function(*args, **kwargs)


    return decorated