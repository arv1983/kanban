
from flask import Flask


def init_app(app: Flask):
    from .signup_view import bp as signup
    app.register_blueprint(signup)
    from .login_view import bp as login
    app.register_blueprint(login)
    from .group_view import bp as group
    app.register_blueprint(group)
    from .post_view import bp as post
    app.register_blueprint(post)    
