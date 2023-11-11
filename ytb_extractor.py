from pytube import YouTube

url = input("Enter the url: ")

my_video = YouTube(url)

print(my_video.title)

for stream in my_video.streams:
    print(stream)

# print(my_video.streams.get_by_itag(247).url)