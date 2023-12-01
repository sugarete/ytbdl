from flask import Flask

# app.register_blueprint(views, url_prefix='/ytdl')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcdefg7749177013'

    from .views import views
    app.register_blueprint(views, url_prefix='/ytdl')
    
    return app