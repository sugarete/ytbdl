from __future__ import unicode_literals
from flask import Flask, request, render_template, send_file, after_this_request
import youtube_dl
import os
app = Flask(__name__, template_folder='app/templates/', static_folder='app/static/')

download_directory = 'downloaded_videos'

if not os.path.exists(download_directory):
    os.makedirs(download_directory)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/d', methods=['GET'])

@app.route('/dl', methods=['POST'])
def download(): 
    if request.method == 'POST':
        url = request.form['url']
        # Use the URL in your command-line script
        ydl_opts = {
            'format': 'best',
            'outtmpl': download_directory + '/%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            video_info = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(video_info)
            # @after_this_request
            # def remove_file(response):
            #     try:
            #         os.remove()
            #     except Exception as error:
            #         print("Error remnoving or closing downloaded file handle", error)
            #     return response  
        return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
