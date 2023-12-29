from flask import Flask

# app.register_blueprint(views, url_prefix='/ytdl')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcdefg7749177013'

    from .views import views
    from .downloads import downloads
    from .auth import auth
    from .easy import easy


    app.register_blueprint(auth, url_prefix='/auth/')
    app.register_blueprint(downloads, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(easy, url_prefix='/dl/')

    return app