
from flask import Flask


def init_app(app: Flask):
    from .signup_views import bp as views

    app.register_blueprint(views)
