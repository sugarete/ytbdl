import os, shutil

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

directory_list = [send_directory, download_video_directory, download_audio_directory, merge_directory]
def clear_directory(directory):
    try:
        print("Clearing directory: ", directory)
        shutil.rmtree(directory)
        print("Creating directory: ", directory)
        os.makedirs(directory)
    except Exception as e:
        print("Error: ", e)

for directory in directory_list:
    clear_directory(directory)