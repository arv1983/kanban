from flask import jsonify, request
from sqlalchemy import Column, String, Integer
from config.db import db
from services.validator import Validator
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token


class UsersModel(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(127), nullable=True)
    api_key = Column(String(511), nullable=True)
    api_key2 = Column(String(511), nullable=True)



    def get_all_users():
        users = []
        for user in UsersModel().query.all():
            users_data = {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
            users.append(users_data)
        return users


    def signup(self):

        validator_response = Validator.signup_validator(self)
                
        if validator_response: 
            return validator_response
        
        self['password'] = generate_password_hash(password=self['password'], salt_length=10)
        data_serialized = UsersModel(**self)
        db.session.add(data_serialized)
        db.session.commit()
    
    def login(self):
        
        validator_response = Validator.login_validator(self)
                
        if validator_response: 
            return validator_response

        email = request.json.get("email", None)
        password = request.json.get("password", None)
        user = UsersModel.query.filter_by(email=email).first()

        if check_password_hash(user.password, password):
            return create_access_token(identity=user.name)
            
        return {'Autorização':'negada'},401
        
        

        