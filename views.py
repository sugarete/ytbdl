from flask import Blueprint, render_template, request
from pytube import YouTube
from flask import Flask, request, render_template, send_file
from urllib.parse import quote
import os
from datetime import timedelta
from moviepy.editor import VideoFileClip, AudioFileClip

views = Blueprint('views', __name__)

download_directory = 'downloaded_videos'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

def format_time(seconds):
    return str(timedelta(seconds=seconds))

@views.route('/')
def home():
    return render_template("home.html")

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

@views.route('/extract', methods=['POST', 'GET'])
def extract():
    if request.method == 'POST':
        url = request.form['url']
        video = YouTube(url)
        return render_template('vidinfo.html', video=video, url = url, format_time=format_time)
    
@views.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    quality = request.args.get('quality')
    
    if url and quality:
        yt = YouTube(url)
        video_url = yt.streams.get_by_itag(quality)

        video_path = video_url.download(download_directory)
        video_clip = VideoFileClip(video_path)
        yt.streams.get_by_itag(140).download(filename="audio.mp4")
        audio_clip = AudioFileClip("audio.mp4")
        final_clip = video_clip.set_audio(audio_clip)

        final_clip.write_videofile("clip.mp4")
        # file_path = os.path.join('q:\\ytbdl-2\\app', 'clip.mp4')
        print("done")
        return send_file('Q:\ytbdl-2\clip.mp4', as_attachment=True)
    else:
        # Handle invalid request (missing parameters)
        return "Invalid request"
