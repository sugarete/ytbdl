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
- [ ] Add user system to charge for downloading (Pay one time for unlimited download)
- [ ] Store download history
- [ ] Edit video (Cut, Merge, Add Sound, Add Subtitle) // Maybe
-----
Update 3/11/2023:  
- run `python ytbdl.py` to start server and open `localhost:80` to use.  
- The current repo have 3 main part:  
    + youtube_dl: The module to download video from Youtube  
    + ytbdl.py: The server to handle request from client and return video  
    + app folder: Contain user interface  

