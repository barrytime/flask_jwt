from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager,
)
from os import environ
from dotenv import load_dotenv
from datetime import timedelta

import routes

load_dotenv()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = environ["JWT_SECRET_KEY"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=60)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=1)
jwt = JWTManager(app)

app.register_blueprint(routes.auth.bp)
app.register_blueprint(routes.api.bp)


@app.route("/")
def home():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=environ["FLASK_DEBUG"], host="0.0.0.0")
