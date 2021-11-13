function time(){

    var today = new Date();

    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();

    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

    var dateTime = date+' '+time;

}
function changeColor(color){
    document.body.style.background = '#'+Math.floor(Math.random()*16777215).toString(16);
}

function reload(){
    window.location.reload()
 }
function openWin(){
    window.open("./index.html");
}
function consoles()
{
console.log("I did it")
}


function nextPage(){
    location.href = "http://127.0.0.1:8080/page-3/chart.html";
}
function saveData(){
    var input = document.getElementById("saveServer");
    localStorage.setItem("server", input.value);
    var storedValue = localStorage.getItem("server");
    console.log(storedValue)
}
function sillystuff(){
    location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
}
