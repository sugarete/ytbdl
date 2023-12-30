from flask import Blueprint, render_template, request, send_file
from pytube import YouTube,Search
from moviepy.editor import VideoFileClip, AudioFileClip
import ffmpeg
import os
from urllib.parse import unquote
from datetime import timedelta

views = Blueprint('views', __name__)

supported_formats = ['mp4', 'mov', 'avi', 'flv', 'm4a', 'wav', '3gp']

# define and create directories if not exist
download_directory = 'downloaded_folder'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# create sub directories for video only
download_video_directory = 'downloaded_folder/videos'
if not os.path.exists(download_video_directory):
    os.makedirs(download_video_directory)

# create sub directories for audio only
download_audio_directory = 'downloaded_folder/audios'
if not os.path.exists(download_audio_directory):
    os.makedirs(download_audio_directory)

# create sub directories for merged video and audio
merge_directory = 'downloaded_folder/merged'
if not os.path.exists(merge_directory):
    os.makedirs(merge_directory)

# create sub directories for send videos
send_directory = 'send_videos'
if not os.path.exists(send_directory):
    os.makedirs(send_directory)
#end of create directories 

# time format from seconds to HH:MM:SS
def format_time(seconds):
    return str(timedelta(seconds=seconds))

# convert audio to mp3
def convert_to_mp3(audio_path):
    try:
        out_audio_path = os.path.join(os.getcwd(), send_directory, os.path.basename(audio_path)[:-4] + '.mp3')
        ffmpeg.input(audio_path).output(out_audio_path).run(overwrite_output=True)
        return out_audio_path
    except Exception as e:
        print("Error: ", e)
        return None

# convert video to selected format
def convert_format(video_path, video_format):
    try:
        out_video_path = os.path.join(os.getcwd(), send_directory, os.path.basename(video_path)[:-4] + '.' + video_format)
        ffmpeg.input(video_path).output(out_video_path, format = video_format).run(overwrite_output=True)
        return out_video_path
    except Exception as e:
        print("Error: ", e)
        return None

# main page routes
@views.route('/')
def home():
    return render_template("search.html")

# extract video info
@views.route('/extract', methods=['POST', 'GET'])
def extract():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            video = YouTube(url)
            return render_template('vidinfo.html', video=video, url = url, format_time=format_time, supported_formats=supported_formats)
        else:
            return "Invalid URL."

# download video
@views.route('/download_video', methods=['GET'])
def download_video():
    print("request.args: ", request.args)
    url = unquote(request.args.get('url'))
    selected_format = request.args.get('format')
    quality = request.args.get('quality')
    # print("url: ", url)
    # print("formats: ", selected_format)
    # print("quality: ", quality)
    if url:
        try:
            yt = YouTube(url)
            video_url = yt.streams.get_by_itag(quality)

            video_path = video_url.download(download_video_directory)
            video_clip = VideoFileClip(video_path)
            audio_path = yt.streams.get_audio_only().download(download_audio_directory)
            audio_clip = AudioFileClip(audio_path)
           
            final_clip = video_clip.set_audio(audio_clip)
            full_video_path = os.path.join(os.getcwd(), merge_directory, os.path.basename(video_path))
            # print("out_video_path: ", out_video_path)
            final_clip.write_videofile(full_video_path)
            
            
            os.remove(video_path)
            os.remove(audio_path)
            if selected_format == 'mp4':
                return send_file(full_video_path, as_attachment=True)
            else:
                out_video_path = convert_format(full_video_path, selected_format)
                os.remove(full_video_path)
                return send_file(out_video_path, as_attachment=True)
        except Exception as e:
            return f"Error: {e}"
    else:
        return "Invalid URL"

# download audio only
@views.route('/download_audio', methods=['GET'])
def download_audio():
    url = request.args.get('url')
    if url:
        try:
            video = YouTube(url)
            audio = video.streams.get_audio_only()
            audio_path = audio.download(download_audio_directory)
            out_audio_path = convert_to_mp3(audio_path)
            if out_audio_path:
                response = send_file(out_audio_path, as_attachment=True)
                os.remove(audio_path)
                return response
            else:
                return "Audio conversion failed."
        except Exception as e:
            return f"Error: {e}"
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
