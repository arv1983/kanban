from flask import Flask, request, jsonify, Blueprint
from models.users_model import UsersModel

bp = Blueprint("login_route", __name__)

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    response = UsersModel.login(data)
    return jsonify(response),200

@bp.route("/", methods=["GET"])
def login2():

    return {'ss': 'ss'}
