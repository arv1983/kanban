from flask import Flask, request, jsonify, Blueprint
# from models.group_model import GroupModel
from models.users_model import UsersModel, GroupsModel
from services.validator import Validator
from config.db import db
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("group_route", __name__)

@bp.route("/group", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    
    
    user = UsersModel.check_user(get_jwt_identity())
    
    validator_response = Validator.group_create_validator(data)
    
    if validator_response:
        return jsonify(validator_response)
    
    data['admin'] = user.id
    


    try:
        data_serialized = GroupsModel(**data)
        db.session.add(data_serialized)
        db.session.commit()
        return {'ss': 'ss'},201
    except:
        return {'deu pau': 'fudeu'}

@bp.route("/join_group/<int:group_id>", methods=["POST"])
@jwt_required()
def join(group_id):
    id = UsersModel.check_user(get_jwt_identity())
    print(id)

    return {'deu pau': group_id}


    
    
    
    



