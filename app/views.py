from flask import Blueprint, render_template, request
from pytube import YouTube
from flask import Flask, request, render_template, send_file, jsonify, redirect, url_for
import os

views = Blueprint('views', __name__)

# download_directory = 'downloaded_videos'
# if not os.path.exists(download_directory):
#     os.makedirs(download_directory)

@views.route('/')
def home():
    return render_template("index.html")

# @views.route('/login')
# def registry():
#     return render_template('login.html')

# @views.route('/signup')
# def signup():
#     return render_template('signup.html')
            
# @views.route('/dl', methods=['POST'])
# def download():
#     if request.method == 'POST':
#         url = request.form['url']
#         video_url = YouTube(url).streams.get_by_itag(22)
#         video = video_url.download(download_directory)
#         return send_file(video, as_attachment=True)
    
# @app.route('/extract', methods=['POST', 'GET']) 
# def extract():
#     if request.method == 'POST':
#         url = request.form['url'x``]
#         video = YouTube(url)
#         video_info = {
#             'title': video.title,
#             'length': video.length,
#         }
#         return jsonify(video_info)
def format_time(seconds):
    return str(timedelta(seconds=seconds))

@views.route('/extract', methods=['POST', 'GET'])
def extract():
    if request.method == 'POST':
        url = request.form['url']
        video = YouTube(url)
        return render_template('vidinfo.html', video=video)
    
# @views.route('/extract/<url>')
# def extract_url(url):
#     video = YouTube(url)
#     return redirect(f"{video.streams.get_highest_resolution().url}",)