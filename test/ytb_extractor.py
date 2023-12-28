import requests
import validators
from pytube import YouTube

url = input("Enter the url: ")

if not validators.url(url):
    print("Invalid url")
    exit()

my_video = YouTube(url)
print(my_video.title)
print(my_video.length)
print(my_video.thumbnail_url)
resolution =[int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in my_video.streams if i.resolution])))]
resolution.sort()

streams = set()
for i in my_video.streams.filter(mime_type="video/mp4", progressive=True):
    streams.add(i.itag)

for itag in my_video.streams:
    print(itag.itag, itag.resolution, itag.mime_type, itag.abr, itag.url)

print("Audio streams----------------------")
for streams in my_video.streams.filter(only_audio=True):
    print(streams, ":", streams.url)

my_video.streams.get_audio_only().download()
my_video.streams.get_by_itag(251).download()

print("Video streams")
print(streams)