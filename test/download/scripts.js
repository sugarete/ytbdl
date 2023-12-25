<script type = "text/javascript" src = "scripts.js"></script>
const urlInput = document.querySelector("Input");
const downloadBtn = document.querySelector("Button");

downloadBtn.addEventListener("click", () => { 
    const url = urlInput.value;
    if (url) {
        chrome.downloads.download({ url });
    }
}
);