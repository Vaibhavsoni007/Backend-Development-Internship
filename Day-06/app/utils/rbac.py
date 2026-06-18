from flask import jsonify
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt
)


def role_required(required_role):

    def wrapper(fn):

        def decorator(*args, **kwargs):

            verify_jwt_in_request()

            claims = get_jwt()

            if claims.get("role") != required_role:
                return jsonify({
                    "error": "Access denied"
                }), 403


            return fn(*args, **kwargs)

        decorator.__name__ = fn.__name__

        return decorator

    return wrapper