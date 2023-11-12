function setAction(action) {
    var form = document.getElementById('download-form');
    var input = document.createElement('input');
    input.type = "text";
    input.name = "url";
    input.value = form.querySelector('input[name="url"]').value;

    form.appendChild(input);

    if(action === 'download') {
        form.action = '/dl';
    } else if(action === 'extract') {
        form.action = '/extract';
    }

    form.submit();
}