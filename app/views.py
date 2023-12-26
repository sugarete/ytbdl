from flask import Blueprint, render_template, request, send_file
from pytube import YouTube
import ffmpeg
from urllib.parse import quote
import os
from datetime import timedelta

views = Blueprint('views', __name__)

download_directory = 'downloaded_videos'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

send_directory = 'send_videos'
if not os.path.exists(send_directory):
    os.makedirs(send_directory)

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

@views.route('/extract', methods=['POST', 'GET'])
def extract():
    if request.method == 'POST':
        url = request.form['url']
        video = YouTube(url)
        return render_template('vidinfo.html', video=video, url = url, format_time=format_time)
    
@views.route('/download_video', methods=['GET'])
def download_video():
    url = request.args.get('url')
    quality = request.args.get('quality')
    
    if url and quality:
        video = YouTube(url)
        video_url = video.streams.get_by_itag(quality)
        video_path = video_url.download(send_directory)
        return send_file(video_path, as_attachment=True)
    else:
        return "Invalid request"

def convert_to_mp3(audio_path):
    out_audio_path = audio_path[:-4] + '.mp3'
    print("Input: " + audio_path)
    print("Output: " + out_audio_path)
    ffmpeg.input(audio_path).output(out_audio_path).run()
    return out_audio_path

@views.route('/download_audio', methods=['GET'])
def download_audio():
    url = request.args.get('url')
    if url:
        # try:
            video = YouTube(url)
            audio = video.streams.get_audio_only()
            audio_path = audio.download(download_directory)
            out_audio_path = convert_to_mp3(audio_path)

            if out_audio_path:
                response = send_file(out_audio_path, as_attachment=True)
                os.remove(audio_path)
                os.remove(out_audio_path)
                return response
            else:
                return "Audio conversion failed."
        # except Exception as e:
        #     return f"Error: {e}"

    return "Invalid URL."
        