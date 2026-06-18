from flask import request, jsonify
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from flask_jwt_extended import create_access_token


def register_auth_routes(app, mysql):

    # Register API
    @app.route("/register", methods=["POST"])
    @limiter.limit("5 per minute")
    def register():

        data = request.get_json()

        username = data.get("username")
        password = data.get("password")
        role = data.get("role", "user")


        if not username or not password:
            return jsonify({
                "error": "Username and password required"
            }), 400


        hashed_password = generate_password_hash(password)


        cursor = mysql.connection.cursor()


        try:
            cursor.execute(
                """
                INSERT INTO users
                (username, password, role)
                VALUES (%s, %s, %s)
                """,
                (
                    username,
                    hashed_password,
                    role
                )
            )

            mysql.connection.commit()


        except Exception as e:

            return jsonify({
                "error": str(e)
            }), 400


        finally:
            cursor.close()


        return jsonify({
            "message": "User registered successfully"
        }), 201


    # Login API
    @app.route("/login", methods=["POST"])
    @limiter.limit("10 per minute")
    def login():

        data = request.get_json()


        username = data.get("username")
        password = data.get("password")


        cursor = mysql.connection.cursor()


        cursor.execute(
            """
            SELECT id, password, role
            FROM users
            WHERE username = %s
            """,
            (username,)
        )


        user = cursor.fetchone()

        cursor.close()


        if not user or not check_password_hash(
            user[1],
            password
        ):
            return jsonify({
                "error": "Invalid credentials"
            }), 401


        token = create_access_token(
        identity=str(user[0]),
        additional_claims={
            "role": user[2]
        }
)


        return jsonify({
            "message": "Login successful",
            "token": token,
            "role": user[2]
        }), 200