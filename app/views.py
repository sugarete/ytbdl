from flask import Blueprint, render_template, request, send_file
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
import ffmpeg
import os
from urllib.parse import unquote
from datetime import timedelta

views = Blueprint('views', __name__)

supported_formats = ['mp4', 'mov', 'avi', 'flv', 'm4a', 'wav', '3gp']

# time format from seconds to HH:MM:SS
def format_time(seconds):
    return str(timedelta(seconds=seconds))

# main page routes
@views.route('/')
def home():
    return render_template("home.html")

# extract video info
@views.route('/extract', methods=['POST', 'GET'])
def extract():
    if request.method == 'GET':
        url = request.args.get('url')
        if url:
            video = YouTube(url)
            return render_template('vidinfo.html', video=video, url = url, format_time=format_time, supported_formats=supported_formats)
        else:
            return "Invalid URL."


