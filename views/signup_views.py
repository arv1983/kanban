from flask import Flask, request, jsonify, Blueprint
from models.users_model import UsersModel


app = Flask(__name__)


@app.route("/")
def signup():
    data = request.get_json()
    response = UsersModel.signup(data)
    return jsonify(response),201
