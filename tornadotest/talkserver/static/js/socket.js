window.onload = init;

function init() {
    var username = prompt("输入用户名")
    var webSocketUri = "ws://localhost:10005/talk";
    var input = document.getElementById('input');
    var socket = new WebSocket(webSocketUri);

    input.onchange = function(){
        var message = username + ':' + input.value;
        socket.send(message);
        input.value = '';
    }

    socket.onopen = function(event){

    }
    socket.onclose = function(event){

    }

    socket.onerror = function(event){
        socket.send('some error');
    }

    socket.onmessage = function(event){
        var message = event.data;
        var node = document.createTextNode(message);
        var div = document.createElement("div");
        div.appendChild(node);
        document.body.insertBefore(div, input);
        input.scrollIntoView();
    }
}