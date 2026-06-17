from flask import Blueprint, request, jsonify
from database.db import mysql
import bcrypt


auth_bp = Blueprint("auth", __name__)


# Register API
@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "user")


    if not username or not email or not password:
        return jsonify({
            "error": "All fields are required"
        }), 400


    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )


    cursor = mysql.connection.cursor()


    query = """
    INSERT INTO users(username, email, password, role)
    VALUES(%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            username,
            email,
            hashed_password,
            role
        )
    )


    mysql.connection.commit()

    cursor.close()


    return jsonify({
        "message": "User registered successfully"
    }), 201



# Login API
@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")


    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()


    if user and bcrypt.checkpw(
        password.encode("utf-8"),
        user[3].encode("utf-8")
    ):

        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user[0],
                "username": user[1],
                "email": user[2],
                "role": user[4]
            }
        })


    return jsonify({
        "error": "Invalid email or password"
    }), 401

@auth_bp.route("/admin", methods=["POST"])
def admin_panel():

    data = request.get_json()

    email = data.get("email")

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT role FROM users WHERE email=%s",
        (email,)
    )

    result = cursor.fetchone()

    cursor.close()

    if result and result[0] == "admin":
        return jsonify({
            "message": "Welcome Admin"
        })

    return jsonify({
        "error": "Access denied. Admin only."
    }), 403