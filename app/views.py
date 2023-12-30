from flask import Blueprint, render_template, request, send_file
from pytube import YouTube,Search
from datetime import timedelta

views = Blueprint('views', __name__)

supported_formats = ['mp4', 'mov', 'avi', 'flv', 'm4a', 'wav', '3gp']

# time format from seconds to HH:MM:SS
def format_time(seconds):
    return str(timedelta(seconds=seconds))

# main page routes
@views.route('/')
def home():
    return render_template("search.html")

# extract video info
@views.route('/extract', methods=['POST', 'GET'])
def extract():
    if request.method == 'GET':
        url = request.args.get('url')
        if url:
            video = YouTube(url)
            return render_template('test.html', video=video, url = url, format_time=format_time, supported_formats=supported_formats)
        else:
            return "Invalid URL."

@views.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    videos = search_youtube(keyword)
    return render_template('search.html', videos=videos)

@views.route('/home')
def home_page():
    url = request.args.get('url')
    return render_template('home.html', url=url)

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
    return render_template('test.html')
