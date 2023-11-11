Project Based Learning 3 Repo: Youtube Downloader
-----
Requirements: C/C++/.NET/Py
- [ ] Connect to Youtube
- [ ] Search Query Processing (Using Google Data API) or (Youtube Data API)
- [ ] Examine HTML to get HTML video's link (OpenSource)
- [ ] Download FLV file - Extract Sound
- [ ] Networking Interface and Download 
-----
Plan: 
- [ ] Change the method: client download video direct from Youtube 
- [ ] Create Quality Selection Menu (1080p, 720p, 480p, 360p, 240p, 144p)
- [ ] Create Extract Sound Menu (Yes/No)
- [ ] Verify user age (18+) to download some video
- [ ] Add user system to charge for downloading (Pay one time for unlimited download)
- [ ] Store download history
- [ ] Edit video (Cut, Merge, Add Sound, Add Subtitle) // Maybe
-----
Update 3/11/2023:  
- Make sure you activate the virtual environment before running the server by running `.venv/Scripts/activate` in the terminal.  
- Run `pip install -r requirements.txt` to install all the required packages.
- Run `python ytbdl.py` to start server and open `localhost:80` to use.  
- The current repo have 3 main part:  
    + youtube_dl: The module to download video from Youtube  
    + ytbdl.py: The server to handle request from client and return video  
    + app folder: Contain user interface  

- GIT HUB TEST