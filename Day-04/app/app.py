from flask import Flask, request, jsonify, g
import os
import bcrypt
import jwt
import datetime
from werkzeug.utils import secure_filename
from db import mysql, configure_db
from functools import wraps


# Create Flask app
app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

UPLOAD_FOLDER = "../uploads"

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg"
}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Configure MySQL
configure_db(app)

def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Flask API is running successfully!"
    })

def token_required(function):

    @wraps(function)
    def decorated(*args, **kwargs):

        token = None

        # Get token from Authorization header
        auth_header = request.headers.get("Authorization")

        if auth_header:
            parts = auth_header.split(" ")

            if len(parts) == 2 and parts[0] == "Bearer":
                token = parts[1]


        if not token:
            return jsonify({
                "message": "Token is missing"
            }), 401


        try:
            data = jwt.decode(
                token,
                app.config["JWT_SECRET_KEY"],
                algorithms=["HS256"]
            )

            # Save user details
            g.user_id = data["user_id"]
            g.email = data["email"]
            g.role = data["role"]


        except jwt.ExpiredSignatureError:
            return jsonify({
                "message": "Token has expired"
            }), 401


        except jwt.InvalidTokenError:
            return jsonify({
                "message": "Invalid token"
            }), 401


        return function(*args, **kwargs)


    return decorated


# Register User API
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data["username"]
    email = data["email"]
    password = data["password"]

    # Convert password into bytes
    password_bytes = password.encode("utf-8")

    # Generate hashed password
    hashed_password = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )

    # Convert hash bytes into string
    hashed_password = hashed_password.decode("utf-8")


    cursor = mysql.connection.cursor()


    query = """
    INSERT INTO users(username, email, password)
    VALUES (%s, %s, %s)
    """


    cursor.execute(
        query,
        (
            username,
            email,
            hashed_password
        )
    )


    mysql.connection.commit()
    cursor.close()


    return jsonify({
        "message": "User registered successfully with secure password"
    }), 201

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data["email"]
    password = data["password"]


    cursor = mysql.connection.cursor()

    query = """
    SELECT id, username, email, password, role
    FROM users
    WHERE email = %s
    """

    cursor.execute(query, (email,))

    user = cursor.fetchone()

    cursor.close()


    # Check if user exists
    if not user:
        return jsonify({
            "message": "User not found"
        }), 404


    stored_password = user[3]


    # Compare entered password with hashed password
    if not bcrypt.checkpw(
        password.encode("utf-8"),
        stored_password.encode("utf-8")
    ):
        return jsonify({
            "message": "Invalid password"
        }), 401


    # Generate JWT Token
    token = jwt.encode(
        {
            "user_id": user[0],
            "email": user[2],
            "role": user[4],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        app.config["JWT_SECRET_KEY"],
        algorithm="HS256"
    )


    return jsonify({
        "message": "Login successful",
        "token": token
    }), 200


@app.route("/upload/<int:user_id>", methods=["POST"])
def upload_file(user_id):

    if "file" not in request.files:
        return jsonify({
            "error": "No file selected"
        }), 400


    file = request.files["file"]


    if file.filename == "":
        return jsonify({
            "error": "File name is empty"
        }), 400


    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)


        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)


        cursor = mysql.connection.cursor()

        query = """
        UPDATE users
        SET profile_image = %s
        WHERE id = %s
        """

        cursor.execute(query, (filename, user_id))

        mysql.connection.commit()

        cursor.close()


        return jsonify({
            "message": "File uploaded successfully",
            "filename": filename
        }), 200


    return jsonify({
        "error": "Invalid file type"
    }), 400


# Get All Users API
@app.route("/users", methods=["GET"])
@token_required
def get_users():

    cursor = mysql.connection.cursor()

    query = """
    SELECT id, username, email, role, created_at
    FROM users
    """

    cursor.execute(query)

    users = cursor.fetchall()

    cursor.close()

    result = []

    for user in users:
        result.append({
            "id": user[0],
            "username": user[1],
            "email": user[2],
            "role": user[3],
            "created_at": user[4]
        })

    return jsonify(result)


# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)