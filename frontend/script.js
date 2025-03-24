elem = document.getElementById('time');

async function update() {
    let res = await fetch('http://77.222.54.5/api/time');
    let json = await res.json();
    elem.innerHTML = json.ans;
}


setInterval(update, 1000);