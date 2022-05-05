from models.users_model import UsersModel
from flask import Flask, request, jsonify, Blueprint

from environs import Env
from config import migrate, db




def create_app() -> Flask:
    app = Flask(__name__)
    env = Env()
    env.read_env()



    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anderson:1234@localhost:5432/kanban'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    
    db.init_app(app)
    migrate.init_app(app)
    
    # views.init_app(app)


    @app.route("/")
    def signup():
        data = request.get_json()
        response = UsersModel.signup(data)
        return jsonify(response),201


    return app


