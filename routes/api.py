from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    jwt_required,
)

bp = Blueprint("api", __name__)


@bp.route("/api")
@jwt_required()
def home():
    return jsonify({"message": "api"})
