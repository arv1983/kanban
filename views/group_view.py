from flask import Flask, request, jsonify, Blueprint
from models.users_model import MembersModel, UsersModel, GroupsModel
from services.validator import Validator
from config.db import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

bp = Blueprint("group_route", __name__)

@bp.route("/create_group", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
        
    user = UsersModel.check_user(get_jwt_identity())
    
    validator_response = Validator.group_create_validator(data)
    
    if GroupsModel.check_group_if_exists_by_name(data['name']).first():
        return {'erro': 'grupo ja existe'},401

    if validator_response:
        return jsonify(validator_response)
    
    data['admin'] = user.id
    
    try:
        data_serialized = GroupsModel(**data)
        db.session.add(data_serialized)
        db.session.commit()
        
        return {'group id': data_serialized.id,
        'group name': data_serialized.name
        },201
    except:
        return {'deu pau': 'fudeu'}

@bp.route("/join_group/<int:group_id>", methods=["POST"])
@jwt_required()
def join(group_id):
    data = {}
    data['groups_id'] = group_id
    data['users_id'] = UsersModel.check_user(get_jwt_identity()).id

    check_group = GroupsModel.check_group_if_exists_by_id(group_id)
    if not check_group:
        return {'Erro': 'Grupo não encontrado.'},404
    
    

    if MembersModel.check_user_in_group(data['users_id'], group_id).all():
        return{'Erro': 'Usuário já cadastrado.'},401
    

    try:
        data_serialized = MembersModel(**data)
        db.session.add(data_serialized)
        db.session.commit()

    except OSError as e:
        print("OS error: {0}".format(e))
        return {'fff':'fff'}


    return {'Grupo': group_id}

@bp.route("/exit_group/<int:group_id>", methods=["POST"])
@jwt_required()
def exit(group_id):
    
    data = {}
    data['groups_id'] = group_id
    data['users_id'] = UsersModel.check_user(get_jwt_identity()).id

    check_user_in_group = MembersModel.check_user_in_group(data['users_id'], group_id).first()
        
    if not check_user_in_group:
        return{'Erro': 'O usuário não está no grupo.'},401

    db.session.delete(check_user_in_group)
    db.session.commit()

    return {'ss': 'ss'}

    
    
    
    



