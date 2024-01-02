from flask import Blueprint, render_template, request, send_file
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment
import ffmpeg, os, shutil
from urllib.parse import unquote

downloads = Blueprint('downloads', __name__)

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

directory_list = [merge_directory, download_audio_directory, download_video_directory, send_directory]

def clear_directory(directory):
    try:
        shutil.rmtree(directory)
        os.makedirs(directory)
    except Exception as e:
        print("Error: ", e)

# convert video to selected format
def convert_format(video_path, video_format):
    try:
        out_video_path = os.path.join(os.getcwd(), download_video_directory, os.path.basename(video_path)[:-4] + '.' + video_format)
        ffmpeg.input(video_path).output(out_video_path, format = video_format).run(overwrite_output=True)
        return out_video_path
    except Exception as e:
        print("Error: ", e)
        return None
    
def merge_video(video_path, audio_path, output_path):
    try:
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)
        video.write_videofile(output_path)
        return output_path
    except Exception as e:
        print("Error: ", e)
        return None

# download video
@downloads.route('/download_video', methods=['GET'])
def download_video():
    print("request.args: ", request.args)
    url = unquote(request.args.get('url'))
    selected_format = request.args.get('format')
    quality = request.args.get('quality')
    enTrim = request.args.get('Trim')
    startTime = request.args.get('startTime')
    endTime = request.args.get('endTime')
    video_only = request.args.get('video_only')
    audio_only = request.args.get('audio_only')
    print("url: ", url + " selected_format: " + selected_format + " quality: " + quality + " enTrim: " + enTrim + " startTime: " + startTime + " endTime: " + endTime + " video_only: " + video_only + " audio_only: " + audio_only )
    if url:
        try:
            yt = YouTube(url)
            audio_path = yt.streams.get_audio_only().download(output_path=download_audio_directory)
            print("audio_path: ", audio_path)
            audio_segment = AudioSegment.from_file(audio_path)  
            if(enTrim == 'true'):
                audio_segment = audio_segment[int(startTime)*1000:int(endTime)*1000]
                out_audio_path = os.path.join(os.getcwd(), send_directory, os.path.basename(audio_path)[:-4] + '.mp3')
                audio_segment.export(out_audio_path, format="mp3")
                if(audio_only == 'true'):
                    return send_file(out_audio_path, as_attachment=True)
                else:
                    video_path = yt.streams.get_by_itag(quality).download(output_path=download_video_directory)
                    video_clip = VideoFileClip(video_path).subclip(int(startTime), int(endTime))
                    out_video_path = os.path.join(os.getcwd(), send_directory, os.path.basename(video_path)[:-4] + '.mp4')
                    video_clip.write_videofile(out_video_path)
                    if(video_only == 'true'):
                        converted_video_path = convert_format(out_video_path, selected_format)
                        return send_file(converted_video_path, as_attachment=True)
                    else:
                        full_video_path = merge_video(out_video_path, out_audio_path, os.path.join(os.getcwd(), merge_directory, os.path.basename(video_path)[:-4] + '.mp4'))
                        converted_full_video_path = convert_format(full_video_path, selected_format)
                        return send_file(converted_full_video_path, as_attachment=True)
            else:
                if(audio_only == 'true'):
                    out_audio_path = os.path.join(os.getcwd(), send_directory, os.path.basename(audio_path)[:-4] + '.mp3')
                    audio_segment.export(out_audio_path, format="mp3")
                    return send_file(out_audio_path, as_attachment=True)
                else:
                    video_path = yt.streams.get_by_itag(quality).download(output_path=download_video_directory)
                    if(video_only == 'true'):
                        converted_video_path = convert_format(video_path, selected_format)
                        return send_file(converted_video_path, as_attachment=True)
                    else:
                        full_video_path = merge_video(video_path, audio_path, os.path.join(os.getcwd(), merge_directory, os.path.basename(video_path)[:-4] + '.mp4'))
                        converted_full_video_path = convert_format(full_video_path, selected_format)
                        return send_file(converted_full_video_path, as_attachment=True)
        except Exception as e:
            return f"Error: {e}"
    else:
        return "Invalid URL"

