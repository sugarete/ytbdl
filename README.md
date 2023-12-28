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
- [ ] Using Youtube Data API to get video's link and search query
- [ ] Change the method: download to server and return link to client
- [ ] Create Quality Selection Menu (1080p, 720p, 480p, 360p, 240p, 144p)
- [ ] Create Extract Sound Menu (Yes/No)
- [ ] Create Video format Menu (mp4, flv, avi, mkv, webm)
- [ ] Create edit video menu (Cut, Merge, Add Sound, Add Subtitle) // Maybe using FFmpeg
- [ ] Store download history
-----
Guide to use Github:  

Guide to run the server:
- Create virutal environment by running `python -m venv .venv` in the terminal.
- Make sure you activate the virtual environment before running the server by running `.venv/Scripts/activate` in the terminal.  
- Run `pip install -r requirements.txt` to install all the required packages.
- Run `python ytbdl.py` to start server and open `localhost:80` to use.  
- The current repo have 3 main part:  
    + youtube_dl: The module to download video from Youtube  
    + ytbdl.py: The server to handle request from client and return video  
    + app folder: Contain user interface  

-----
Update: 25/12/2023:
Thay đổi cách thức hoạt động của server:
Tải video về server và send file về client, mục đích tải về server là để có thể xử lý video (cắt, ghép, thay đổi định dạng)
- [x] Cho phép lựa chọn chất lượng video tải về (FLV) !(tuy nhiên vẫn còn gặp nhiều hạn chế khi chọn các chất lượng không đi kèm với âm thanh)  
- [x] Cho phép lựa chọn tải audio riêng MP3  - Pytube
- [ ] Search Query Processing - Youtube Data API hoặc Pytube
- [ ] Lưu lịch sử tải về 
- [ ] Cắt video tại thời điểm được chỉ định (Làm UI cho phần lựa chọn) - Pytube hoặc FFmpeg 
- [ ] Cho phép lựa chọn định dạng video tải về (mp4, flv, avi, mkv, webm)  - FFmpeg

