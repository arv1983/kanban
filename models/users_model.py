from flask import Flask, jsonify, request, session
from sqlalchemy import Column, Date, ForeignKey, String, Integer, and_, or_
import sqlalchemy
from sqlalchemy.orm import relationship, backref
from config.db import db
from services.validator import Validator
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from dataclasses import dataclass
from datetime import datetime

class UsersModel (db.Model):
    __tablename__ = "tb_users"
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.Unicode)
    email = db.Column('email', db.Unicode)
    password = db.Column('password', db.Unicode)
    

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
        

        if UsersModel.check_user(self['email']):
            return {'Erro': 'email já cadastrado'},401



        self['password'] = generate_password_hash(password=self['password'], salt_length=10)
        
        try:
            data_serialized = UsersModel(**self)
            db.session.add(data_serialized)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            print('psycopg2.errors.UniqueViolation')
            print(e)
            return {'unique': 'ss'}
        return '',201



    
    def login(self):
        
        validator_response = Validator.login_validator(self)

                      
        if validator_response: 
            return validator_response,401

        email = request.json.get("email", None)
        password = request.json.get("password", None)
        
        
        user = UsersModel.check_user(email)
        
        if not user:
            return {'Erro': 'email não encontrado'},401

        

        if check_password_hash(user.password, password):
            return {'token': create_access_token(identity=user.email)},200
            
        return {'Autorização':'Negada', 'Motivo':'senha inválida'},401
    

    def check_user(user):

        user = UsersModel.query.filter_by(email=user).first()
        print(user)
        return user





class GroupsModel (db.Model):
    
    __tablename__ = "tb_groups"
    id = db.Column('id', db.Integer, primary_key=True)
    admin = db.Column('admin', db.Integer, db.ForeignKey('tb_users.id'))
    name = db.Column('name', db.Unicode)

    usersmodel = db.relationship('UsersModel', foreign_keys=admin)


    # def join(user):

    #     cliente = UsersModel.query.filter_by(email=user).first()
    #     if not cliente:
    #         raise AttributeError(
    #             {"Error": "Usuario nao encontrado"}
    #         )
    #     return cliente    
    
    def check_group_if_exists_by_id(id_group):
        group = GroupsModel.query.filter_by(id=id_group).first()

        if not group:
            return False
        return True

    def check_group_if_exists_by_name(group_name):
        
        produtos = GroupsModel.query.filter(
            GroupsModel.name.like((f'%{group_name}%')) 
        )
        return produtos

    def check_admin(group_id, user_id):
        group = GroupsModel.query.filter_by(id=group_id).first()

        if(group.admin == user_id):
            return True
        return False



class PostModel (db.Model):
    __tablename__ = "tb_post"
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.Unicode)
    description = db.Column('description', db.Unicode)
    
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('tb_users.id'))
    group_id = db.Column('group_id', db.Integer, db.ForeignKey('tb_groups.id'))
    
    def record_post(data):
        print(data)
        
        try:
            data_serialized = PostModel(**data)
            db.session.add(data_serialized)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            return {'unique': e}
        return data_serialized

    def check_post_of_groupid(post_id, group_id):
        
        return PostModel.query.filter(PostModel.id == post_id, PostModel.group_id == group_id)

    def record_edit_post(data):
            seri = PostModel(**data)
            db.session.add(seri)
            db.session.commit()





class MembersModel (db.Model):
    __tablename__ = "tb_members"
    id = db.Column('id', db.Integer, primary_key = True)
    # id_group = db.Column('id_group', db.Integer)
    # id_member = db.Column('id_member', db.Integer, db.ForeignKey('post.id'))
    date = db.Column('date', db.DateTime)
    users_id = db.Column('users_id', db.Integer, db.ForeignKey('tb_users.id'))
    groups_id = db.Column('groups_id', db.Integer, db.ForeignKey('tb_groups.id'))

    # post = db.relationship('Post', foreign_keys=id_member)
    usersmodel = db.relationship('UsersModel', foreign_keys=users_id)

    


    def check_user_in_group(user_id, group_id):
 
        member_in_group = MembersModel.query.filter(MembersModel.groups_id == group_id, MembersModel.users_id == user_id)
        
        return member_in_group

        










# @dataclass
# class MembersModel(db.Model):
#     __tablename__ = "members"
#     id = Column(primary_key=True)
#     id_group = Column(Integer, ForeignKey('groups.id'), nullable=False)
#     id_member = Column(Integer, ForeignKey('users.id'), nullable=False)
#     data = Column(String(127), nullable=True)



# class GroupModel(db.Model):
#     __tablename__ = "groups"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(127), nullable=False)

#     admin = Column(Integer, ForeignKey('users.id'))

#     # members = Column(Integer, ForeignKey('members.id'))

#     members = relationship("MembersModel", backref='users_pivo', lazy=True)

# class PostsModel(db.Model):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     group = Column(String(127), nullable=False)
#     autor = Column(ForeignKey("users.id"), nullable=False)
    
    
    
#     signed = Column(Integer, ForeignKey('users.id'))
#     signed_id = relationship("users", foreign_keys=[signed], backref='users_pivo')
    




#     progress = Column(Integer, ForeignKey('state.id'))

#     title = Column(String(255), nullable=False)
#     description = Column(String(255), nullable=False)
#     date = Column(Date, nullable=False)
    
# class StateModel(db.Model):
#     __tablename__ = "state"
#     id = Column(Integer, primary_key=True)
#     signed = Column(Integer, ForeignKey('users.id'))
#     progress = Column(Integer, nullable=False)
#     date = Column(Date, nullable=False)