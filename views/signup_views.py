from flask import Flask, request, jsonify, Blueprint
from models.users_model import UsersModel

bp = Blueprint("signup_route", __name__)

@bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    
    response = UsersModel.signup(data)
    return jsonify(response),201
