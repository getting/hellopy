/**
 * 利用getUserMedia api 启用摄像头 并实现视频截图
 * 只能在Chrome 下使用
 */

var video = document.querySelector('video');
var canvas = document.querySelector('canvas');
var ctx = canvas.getContext('2d');
var startButton = document.getElementById('start-button');
var snapshotButton = document.getElementById('snapshot-button');

var snapshot = function() {
    ctx.drawImage(video, 0, 0, 300, 150);
    document.querySelector('img').src = canvas.toDataURL('image/webp');
}

var onFailSoHard = function (e) {
    alert('请同意权限请求');
};

var videoOn = function() {
    if (navigator.webkitGetUserMedia) {
        var video = document.querySelector('video');
        navigator.webkitGetUserMedia({'audio': true, 'video': true}, function (localMediaStream) {
            var video = document.querySelector('video');
            video.src = window.webkitURL.createObjectURL(localMediaStream);
        }, onFailSoHard);
    } else {
        alert('您的浏览器暂时不支持该功能');
    }
}

snapshotButton.addEventListener('click', snapshot, false);
startButton.addEventListener('click', videoOn, false);
