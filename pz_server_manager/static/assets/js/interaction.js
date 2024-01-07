function interact(btn) {
    fetch('/interaction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ interaction: btn })
    }).then(response => response.json())
        .then(data => console.log(data));
}

function fetch_collection() {
    fetch('/interaction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ interaction: 'fetch_collection' })
    }).then(response => response.json())
        .then(data => {
            modlist = document.getElementById('modlist');
            modlist.innerHTML = data.result;
            document.getElementById("modcount").innerText= "Mods in Collection: " + modlist.childElementCount;
        });
}