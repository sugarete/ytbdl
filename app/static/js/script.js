function setAction(action) {
    document.getElementById('download-form').action = action;
}

function extractVideoInfo() {
    var url = document.getElementById('url').value;
    
    fetch('/extract', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'url=' + encodeURIComponent(url),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        displayVideoInfo(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayVideoInfo(data) {
    var videoInfoDisplay = document.getElementById('videoInfoDisplay');
    var htmlContent = '<h2>Video Information</h2>';
    htmlContent += '<p>Title: ' + data.title + '</p>';
    htmlContent += '<p>Length: ' + data.length + ' seconds</p>';
    videoInfoDisplay.innerHTML = htmlContent;
}