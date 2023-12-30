from flask import Blueprint, render_template, request, send_file
from pytube import YouTube
import os
from urllib.parse import unquote

easy = Blueprint('easy', __name__)

# create sub directories for send videos
send_directory = 'send_videos'
if not os.path.exists(send_directory):
    os.makedirs(send_directory)
#end of create directories 
    
@easy.route('/video', methods=['GET'])
def download_easy_video():
    url = request.args.get('url')
    if url:
        video = YouTube(url)
        video_path = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=send_directory)
        return send_file(video_path, as_attachment=True)
    else:
        return "Invalid URL."
    
@easy.route('/audio', methods=['GET'])
def download_easy_audio():
    url = request.args.get('url')
    if url:
        video = YouTube(url)
        audio_path = video.streams.filter(only_audio=True).first().download(output_path=send_directory)
        return send_file(audio_path, as_attachment=True)
    else:
        return "Invalid URL."