from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db
    # from models.state_post_model import StateModel
    from models.users_model import UsersModel
    # from models.group_model import GroupModel
    # from models.members_model import MembersModel
    # from models.posts_model import PostsModel
