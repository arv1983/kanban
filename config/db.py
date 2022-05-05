from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from models.users_model import UsersModel