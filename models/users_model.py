from flask import request
from sqlalchemy import Column, String, Integer
from config.db import db
from services.signup import ValidatorSignup
from werkzeug.security import check_password_hash, generate_password_hash



class UsersModel(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False)
    email = Column(String(255), nullable=False)
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

        validator_response = ValidatorSignup.signup_validator(self)
                
        if validator_response: 
            return validator_response
        
        self['password'] = generate_password_hash(password=self['password'], salt_length=10)
        data_serialized = UsersModel(**self)
        db.session.add(data_serialized)
        db.session.commit()
    
    def login(self):

        ...... continua a validacao aqui
        email = request.json.get("email", None)
        password = request.json.get("senha", None)
        user = UsersModel.query.filter_by(email=email).first()
        
        print(user)
        