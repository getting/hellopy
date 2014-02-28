# 二维码生成api

----

接口地址：http://qrcoder.sinaapp.com/

## 简单使用

参数t指定生成的二维码中将要包含的文本

举个栗子：

http://qrcoder.sinaapp.com?t=hello world

生成的二维码中将包含'hello world'的文本信息

在网页中简单引用：
`<img src="http://qrcoder.sinaapp.com?t=hello world">`


## 进阶使用

http://qrcoder.sinaapp.com?t=hello world&f=json

将返回json格式的二维码信息

返回格式：

{"url": "http://qrcoder-image.stor.sinaapp.com/aGVsbG8gd29ybGQ=.png", "text": "hello world"}

text： 输入的文本
url： 生成二维码图片的地址