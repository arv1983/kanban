from flask import Flask, request, jsonify, Blueprint

from models.users_model import GroupsModel, MembersModel, PostModel, UsersModel
from services.validator import Validator

bp = Blueprint("post_route", __name__)
from flask_jwt_extended import jwt_required, get_jwt_identity


@bp.route("/post/<int:group_id>", methods=["POST"])
@jwt_required()
def post(group_id):

    data = request.get_json()
    validator_response = Validator.post_create_validator(data)    

    if validator_response:
        return jsonify(validator_response),401
    
    data['user_id'] = UsersModel.check_user(get_jwt_identity()).id
    data['group_id'] = group_id

    if not GroupsModel.check_group_if_exists_by_id(data['group_id']):
        return {'Erro': 'Grupo não encontrado.'},404
    
    if not len(MembersModel.check_user_in_group(data['user_id'], group_id).all()) > 0 and not GroupsModel.check_admin(data['group_id'], data['user_id']):
        return {'Erro': 'Você não está neste grupo'},401  

    record = PostModel.record_post(data)
    
    return jsonify({'id': record.id, 'titulo': record.title, 'postagem': record.description}),201