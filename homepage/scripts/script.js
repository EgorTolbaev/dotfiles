// Поиск
document.getElementById("search-field").addEventListener("keydown",  event => {
    if (event.keyCode === 13) {
        var val = document.getElementById("search-field").value;
        window.open("https://duckduckgo.com/?q=" + val);
    }
});
// Получить текущее время и формат
getTime = () => {
    let date = new Date(),
        min = date.getMinutes(),
        sec = date.getSeconds(),
        hour = date.getHours();

    return "" +
        (hour < 10 ? ("0" + hour) : hour) + ":" +
        (min < 10 ? ("0" + min) : min) + ":" +
        (sec < 10 ? ("0" + sec) : sec);
}

window.onload = () => {
    // Настройка часов
    document.getElementById("clock").innerHTML = getTime();
    // Установим интервал времени, чтобы часы тикали
    setInterval( () => {
        document.getElementById("clock").innerHTML = getTime();
    },100);
}

document.addEventListener("keydown", event => {
    if (event.keyCode == 32) {          // Spacebar открыть поиск
        document.getElementById('search').style.display = 'flex';
	setTimeout("document.getElementById('search-field').focus()", 500);
    } else if (event.keyCode == 27) {   // Esc закрыть поиск
        document.getElementById('search-field').value = '';
        document.getElementById('search-field').blur();
        document.getElementById('search').style.display = 'none';
    }
});
