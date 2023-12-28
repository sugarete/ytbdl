from flask import Blueprint, render_template, request, send_file
from pytube import YouTube
import ffmpeg
from urllib.parse import unquote
import os
from datetime import timedelta

views = Blueprint('views', __name__)

download_directory = 'downloaded_videos'
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

send_directory = 'send_videos'
if not os.path.exists(send_directory):
    os.makedirs(send_directory)

supported_formats = ['mp4', 'mov', '3gp', 'avi', 'webm', 'flv', 'mkv', 'm4a']

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
        return render_template('vidinfo.html', video=video, url = url, format_time=format_time, supported_formats=supported_formats)
    
@views.route('/download_video', methods=['GET'])
def download_video():
    print("request.args: ", request.args)
    url = unquote(request.args.get('url'))
    formats = request.args.get('formats')
    quality = request.args.get('quality')
    print("url: ", url)
    print("formats: ", formats)
    print("quality: ", quality)
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
#         video = YouTube(url)
#         video_url = video.streams.get_by_itag(quality)
#         video_path = video_url.download(send_directory)
#         print("video_path: ", video_path)
#         return send_file(video_path, as_attachment=True)
    else:
        return "Invalid request"

def convert_to_mp3(audio_path):
    out_audio_path = os.path.join(os.getcwd(), send_directory, os.path.basename(audio_path)[:-4] + '.mp3')
    # out_audio_path = audio_path[:-4] + '.mp3'
    ffmpeg.input(audio_path).output(out_audio_path).run(overwrite_output=True)
    return out_audio_path

@views.route('/download_audio', methods=['GET'])
def download_audio():
    url = request.args.get('url')
    if url:
        try:
            video = YouTube(url)
            audio = video.streams.get_audio_only()
            audio_path = audio.download(download_directory)
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

def format_convert():
    return
