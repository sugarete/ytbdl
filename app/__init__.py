from flask import Flask

# app.register_blueprint(views, url_prefix='/ytdl')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcdefg7749177013'

    from .views import views
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(views, url_prefix='/')

    return app