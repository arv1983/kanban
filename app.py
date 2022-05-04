from copyreg import pickle
from models.users_model import UsersModel
from flask import Flask, request, jsonify
from environs import Env
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config.db import db


app = Flask(__name__)
env = Env()
env.read_env()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anderson:1234@localhost:5432/kanban'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSON_SORT_KEYS"] = False


db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)
migrate.init_app(app, db)

@app.route("/")
def signup():

    data = request.get_json()

    response = UsersModel.signup(data)
    

    return jsonify(response),201




