from __future__ import unicode_literals
from flask import Flask
from views import views

app = Flask(__name__, template_folder='app/templates/', static_folder='app/static/')
app.register_blueprint(views, url_prefix='/ytdl')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)
