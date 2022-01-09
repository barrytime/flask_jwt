from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)
from authenticate import authenticate

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = authenticate(username, password)
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=user, expires_delta=current_app.config["JWT_ACCESS_TOKEN_EXPIRES"]
    )
    refresh_token = create_refresh_token(
        identity=user, expires_delta=current_app.config["JWT_REFRESH_TOKEN_EXPIRES"]
    )
    return (
        jsonify(identity=user, access_token=access_token, refresh_token=refresh_token),
        200,
    )


@bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token), 200
