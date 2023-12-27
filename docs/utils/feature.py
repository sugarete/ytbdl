from __future__ import unicode_literals
from flask import Flask, request, render_template, send_file, jsonify
from pytube import YouTube,Search
from io import BytesIO
import os
# from moviepy.editor import VideoFileClip

# def trim_download():
#     if request.method == 'POST':
#         url = request.form['url']
#         FILE_NAME_DOWNLOADED_VIDEO = 'downloaded_video.mp4'
#         FILE_NAME_TRIMMED_VIDEO = 'trimmed_video.mp4'
#         video_url = YouTube(url).streams.filter(res="720p").first()
#         video_url.download(filename=FILE_NAME_DOWNLOADED_VIDEO)
#         clip = VideoFileClip(FILE_NAME_DOWNLOADED_VIDEO)
#         trimmed_video = clip.subclip(100, 200) # cut tu 100s-200s 
#         trimmed_video.write_videofile(FILE_NAME_TRIMMED_VIDEO)
#         return send_file(FILE_NAME_TRIMMED_VIDEO, as_attachment=True)
    
def search_key_word():
    if request.method == 'POST':
        key_word=request.form['keywords']
        print(key_word)
        s=Search(key_word)
        s.results                       
      
        for v in s.results:
         print(f"{v.title}\n{v.watch_url}\n")

        
        #keys = "\n".join([k for k in s.results[0].__dict__])
        # print(keys)
        return s.results