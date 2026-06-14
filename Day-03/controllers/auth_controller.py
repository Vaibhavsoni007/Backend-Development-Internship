from flask import request, jsonify, current_app
import jwt
import datetime
from models.user_model import User
from extensions import db, bcrypt


def register_user():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # Check email already exists
    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return jsonify({
            "message": "Email already registered"
        }), 400

    # Hash password
    hashed_password = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    # Create user object
    user = User(
        name=name,
        email=email,
        password=hashed_password
    )

    # Save to database
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201

def login_user():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")


    # Check user exists
    user = User.query.filter_by(
        email=email
    ).first()


    if not user:
        return jsonify({
            "message": "Invalid email or password"
        }), 401


    # Compare password
    if not bcrypt.check_password_hash(
        user.password,
        password
    ):
        return jsonify({
            "message": "Invalid email or password"
        }), 401


    # Generate JWT Token
    token = jwt.encode(
        {
            "user_id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(hours=1)
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )


    return jsonify({
        "message": "Login successful",
        "token": token
    }), 200

def get_profile():

    return jsonify({
        "message": "Welcome to your profile",
        "data": {
            "name": "Mohan",
            "role": "Authenticated User"
        }
    }), 200