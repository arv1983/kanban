from crypt import methods
from models.users_model import UsersModel
from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import JWTManager
from environs import Env
from config import migrate, db
import views
# from app import views



bp = Blueprint('auth', __name__, url_prefix='/auth')

def create_app() -> Flask:
    app = Flask(__name__)
    env = Env()
    env.read_env()
    jwt = JWTManager()



    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://grwqqpdhhrutgk:b9a964ee98cc11f73dc94171a3cc1771d80016efe134e401e19babfcdd6ed5cb@ec2-52-204-195-41.compute-1.amazonaws.com:5432/dc2gvkdurje1kt'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anderson:1234@localhost:5432/kanban'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["JWT_SECRET_KEY"] ="pass"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False  
    
    db.init_app(app)
    migrate.init_app(app)
    jwt.init_app(app)
    views.init_app(app)

    
    return app


