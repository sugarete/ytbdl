from flask import Blueprint, render_template, request, send_file,session
from pytube import YouTube,Search
from urllib.parse import unquote
from datetime import timedelta
import re, os, shutil
from .downloads import directory_list, clear_directory
from .connect_db import write_history, get_now, get_history

views = Blueprint('views', __name__)

supported_formats = ['mp4', 'mov', 'avi', 'flv', 'dash', 'mpeg']

# time format from seconds to HH:MM:SS
def format_time(seconds):
    return str(timedelta(seconds=seconds))

def is_url_valid(url):
    url_regex = r"https?://([0-9a-zA-Z-_])"
    if re.match(url_regex, url):
        return True
    else:
        return False
    
@views.after_request
def set_headers(response):
    response.headers["Referrer-Policy"] = 'no-referrer'
    return response

# main page routes
@views.route('/')
def home():
    for directory in directory_list:
        clear_directory(directory)
    username = session.get('username')
    print(username)
    return render_template("home.html", username=username, history = get_history("select time, link, videoname from history where username = ?", (username,)))


# extract video info
@views.route('/extract', methods=['POST', 'GET'])
def extract():
    
    for directory in directory_list:
        clear_directory(directory)

    if request.method == 'GET':
        url = request.args.get('url')
        if url:
            video = YouTube(url)
            if session.get('username') is not None:
                sql = "insert into history (time, link, username, videoname) values (?, ?, ?, ?)"
                write_history(sql, (get_now(), url, session.get('username'), video.title))
            video_id = video.video_id
            return render_template('detail.html', video=video, url = url, format_time=format_time, supported_formats=supported_formats, video_id=video_id)
        else:
            return "Invalid URL."

@views.route('/search', methods=['GET'])
def search():
    keyword = unquote(request.args.get('url'))
    if (is_url_valid(keyword)):
        return render_template('home.html', url = keyword)
    else:
        username = session.get('username')
        videos = search_youtube(keyword)
        return render_template('home.html', videos=videos, show_results=True, username = username, history = get_history("select time, link, videoname from history where username = ?", (username,)))

@views.route('/home')
def home_page():
    url = request.args.get('url')
    username = session.get('username')
    return render_template('home.html', url=url, username=username, history = get_history("select time, link, videoname from history where username = ?", (username,)))

def search_youtube(keyword):
    videos = []
    try:
        # Use pytube to perform the search
        search_results = Search(keyword).results
        for video in search_results:
            videos.append({
                'title': video.title,
                'video_id': video.video_id,
                'thumbnail': video.thumbnail_url,
                'url': f'https://www.youtube.com/watch?v={video.video_id}'
            })
    except Exception as e:
        print(f"An error occurred: {e}")
    return videos

@views.route('/test')
def test():
    return render_template('test2.html')
