from pytube import YouTube

url = input("Enter the url: ")

my_video = YouTube(url)
print(my_video.title)
print(my_video.length)
print(my_video.thumbnail_url)
for stream in my_video.streams:
    print(stream)
    print(stream.resolution)

print(my_video.streams.get_by_itag(22).url);
    