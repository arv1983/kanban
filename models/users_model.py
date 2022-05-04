from sqlalchemy import Column, String, Integer
from config.db import db
from dataclasses import dataclass

from services.signup import ValidatorSignup



class UsersModel(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False)
    email = Column(String(255), nullable=False)
    password_hash = Column(String(127), nullable=True)
    api_key = Column(String(511), nullable=True)



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

        # SIGNUP = ["name", "email", "password"]
        # requered = [req for req in SIGNUP if req not in self]
        # if requered:
        #     response = {
        #         "Erro": "Faltam campos obrigatórios",
        #         "recebido": [inf for inf in self],
        #         "faltantes": {
        #             "Campos": requered,
        #         },
        #     },
        #     return response
        validator_response = ValidatorSignup.signup_validator(self)
                
        if validator_response: 
            return validator_response



  
        data_serialized = UsersModel(**self)
        db.session.add(data_serialized)
        db.session.commit()







        
