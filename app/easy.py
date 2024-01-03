from flask import Blueprint, render_template, request, send_file, session, redirect, url_for
from pytube import YouTube
from .downloads import directory_list, clear_directory
import os
import datetime
from .connect_db import write_history, get_now

easy = Blueprint('easy', __name__)

# create sub directories for send videos
send_directory = 'send_videos'
if not os.path.exists(send_directory):
    os.makedirs(send_directory)
#end of create directories 
    
# cur.execute("insert into history (time, link, userid) values (?, ?, ?)", (now, 'https://www.youtube.com/watch?v=6Dh-RL__uN4', 1))
@easy.route('/video', methods=['GET'])
def download_easy_video():
    for directory in directory_list:
        clear_directory(directory)
    url = request.args.get('url')
    if url:
        print("Downloading video form ", url)
        video = YouTube(url)
        if session.get('username') is not None:
            sql = "insert into history (time, link, username, videoname) values (?, ?, ?, ?)"
            write_history(sql, (get_now(), url, session.get('username'), video.title))
        video_path = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=send_directory)
        redirect_delay = 5000  # 5 seconds delay
        redirect_url = url_for('views.home')  # Replace with the actual URL
        redirect_js = f"setTimeout(function(){{window.location.href = '{redirect_url}';}}, {redirect_delay});"
        return send_file(video_path, as_attachment=True) and redirect(url_for('views.home'))
    else:
        return "Invalid URL."
    
@easy.route('/audio', methods=['GET'])
def download_easy_audio():
    for directory in directory_list:
        clear_directory(directory)
    url = request.args.get('url')
    if url:
        video = YouTube(url)
        if session.get('username') is not None:
            sql = "insert into history (time, link, username, videoname) values (?, ?, ?, ?)"
            write_history(sql, (get_now(), url, session.get('username'), video.title))
        audio_path = video.streams.filter(only_audio=True).first().download(output_path=send_directory)
        return send_file(audio_path, as_attachment=True) and redirect(url_for('views.home'))
    else:
        return "Invalid URL."