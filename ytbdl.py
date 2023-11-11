from __future__ import unicode_literals
from flask import Flask, request, render_template, send_file, jsonify
from pytube import YouTube
from io import BytesIO
import os
app = Flask(__name__, template_folder='app/templates/', static_folder='app/static/')

download_directory = 'downloaded_videos'

if not os.path.exists(download_directory):
    os.makedirs(download_directory)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/login')
def registry():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
            
@app.route('/dl', methods=['POST'])
def download():
    if request.method == 'POST':
        url = request.form['url']
        video_url = YouTube(url).streams.get_by_itag(22)
        video = video_url.download(download_directory)
        return send_file(video, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)