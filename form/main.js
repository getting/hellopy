window.onload = function(){
    var message = document.getElementById('message');
    var content = document.getElementById('content');
    var count = document.getElementById('count');
    message.onkeydown = change
    message.onkeyup = change

    function change(){
        //实时显示输入
        content.innerHTML = message.value;
        //字数统计
        var length = message.value.length;
        count.innerHTML = length > 0 ? length : '';
    }
}