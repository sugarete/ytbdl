from __future__ import unicode_literals
from flask import Flask, request, render_template, send_file, jsonify
from pytube import YouTube,Search
from io import BytesIO
import os
from moviepy.editor import VideoFileClip


def cut(url,t_start,t_end):
    yt = YouTube(url)
    video_stream = yt.streams.filter(only_video=True).first()                   
    video_stream.download(filename='video.mp4')
    clip = VideoFileClip('video.mp4') 
    clip = clip.subclip(t_start, t_end)
    return clip

def convert_gif():
    if request.method == 'POST':
       
        url = request.form['url']
        time1=1 #lay tu request html
        time2=10  #lay tu request html
        time=time2-time1
        clip=cut(url,time1,time2)        
        
        if time < 20:           
                # gif=VideoFileClip('video.mp4')
            clip.write_gif('gif.gif',fps=10)
                # video2gif = VideoFileClip("gif.gif")              
            print("send file success")
            return send_file('gif.gif',as_attachment=True)
        else:
            err='xu ly loi  abc'
            return  err
        # return send_file('gif.gif',as_attachment=True)
        return 0