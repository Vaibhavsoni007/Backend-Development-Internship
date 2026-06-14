from flask import Blueprint
from controllers.auth_controller import (
    register_user,
    login_user,
    get_profile
)
from middleware.auth_middleware import token_required


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    return register_user()


@auth_bp.route("/login", methods=["POST"])
def login():
    return login_user()

@auth_bp.route("/profile", methods=["GET"])
@token_required
def profile():
    return get_profile()