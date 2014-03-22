问题1: 爬取tv.sohu.com的页面, 提取视频相关信息，不可用爬虫框架完成

需求:

做到最大可能的页面覆盖率
选择重要的信息进行存储
选择合适的数据存储方式，便于后续使用
可通过参数限制要抓取视频信息的数目
要用多线程方式完成抓取
反防抓取策略
*分布式支持
*崩溃后进度恢复
星号部分为加分项, 可只给出设计思路 ...




数据采用MongoD存储

主要有两个集合：
url   存储已经收集到的地址：主要用于比对和去重，防止重复抓取
    url: 原始链接地址
    id: 原始链接地址的hash值，用于快速比对

tv    用于存储获取的视频信息

由于视频分类不同，对于一般的视频信息采集，页面head部分的信息已经足够丰富，如果需要，大概
    ### 对于视频页面的分析

    div class=infoBox cfix  id=info
    <div class="info info-con">
    <div class="area cfix" id="content">

    <meta http-equiv="content-type" content="text/html; charset=GBK" />
<meta name="keywords" content="" />
<meta name="description" content="《中国梦之声》20130825 总决选,《中国梦之声》是东方卫视引进世界《偶像Idol》版权所打造的中国电视史上最强的超大型歌唱选秀节目。该节目将于5月19日登陆东方卫视。这也是中国所引进的最大规模、最具影响力的电视真人秀节目。由李玟、韩红、黄晓明、王伟忠四人担任该节目明星导师，为中国乐坛的发展选拔一批怀揣梦想、具有天赋才华的音乐人，树立中国电视音乐节目的新..." />
<meta name="robots" content="all" />
<meta name="album" content="中国梦之声" />
<meta name="category" content="综艺" />
<meta property="og:videosrc" content="http://share.vrs.sohu.com/1291150/v.swf&autoplay=false" />
<meta property="og:url" content="http://tv.sohu.com/20130826/n385016735.shtml"/>
<meta property="og:type" content="video"/>
<meta property="og:video" content="http://share.vrs.sohu.com/1291150/v.swf&autoplay=false"/>
<meta property="og:video:type" content="application/x-shockwave-flash"/>
<meta property="og:site_name" content="搜狐视频" />
<meta property="og:title" content="《中国梦之声》20130825 总决选 - 搜狐视频" />
<meta property="og:image" content="http://photocdn.sohu.com/20130826/vrsb941518.jpg" />
<meta name="mobile-agent" content="format=html5;url=http://m.tv.sohu.com/20130826/n385016735.shtml">





线程需要处理的url加入队列，减少自行加锁的复杂

queue  存储待处理的url队列
queue_tv  需要提取视频信息的url队列

采用广度优先算法，从一个入口(首页）地址开始，将地址加入队列，并存储到已抓取的url集合中，将存储在队列中的地址取出并找出对应页面全部url地址，
将得到的地址与已经抓取的url集合进行对比，如果url集合中尚不存在，加入集合，并加入队列。重复操作，知道寻找到所有链接。


目前是一边抓取新的地址，一边对符合视频页规则的页面进行解析和视频信息提取，或许将两者分开进行效果会更好些。


数据存储在MongoDB，为提高性能对于已经抓取的url可以用redis存储和进行去重比对。广度优先可能会采集很多重读的url在数据库中已知url变多时，从中
进行查询和对比可鞥会很慢，可以将类似首页等最容易出现重复的部分，单独存储在一个列表中，在去重对比时先对比这个小的列表，如果重复则不再需要查询数据库。



分布式可以利用MongoDB的分片？

按url类型，用户上传，和光放上传，或按照时期进行切分，分布到不同的机器上处理

崩溃后的恢复？
设置连接超时，在第一次超时后重新尝试链接？
所有已经遍历的地址存储在数据库中在一个地址被成功处理后可以做一条标记，在崩溃后重新从未标记的位置开始搜索。




页面body部分信息不够统一，重要信息在head中已经包含
页面信息直接从head获取

从http://tv.sohu.com 或 http://tv.sohu.com/map 开始抓取，似乎没有大的区别，



只抓取单独的视频页，不抓取分类和剧集等页面信息


主要有两种类型

官方发布的视频：http://tv.sohu.com/20140304/n395970803.shtml
日期 + 编号

用户上传的视频：http://my.tv.sohu.com/us/200430155/63582287.shtml
用户id + 编号


崩溃后恢复



视频总数估算

百度搜索 site:tv.sohu.com
83,100,000

Google
17,300,000


独立的视频页面（扣除各种主页目录，分类，分页页面等）

3000 00000   / 3

1000 00000


当前中文维基百科在各语言维基百科条目数排名中列第15名，目前已拥有757,023条条目。
页面：3,348,660
site:zh.wikipedia.org
Google  2,000,000
Baidu 13,400,000

http://zh.wikipedia.org/wiki/Special:%E7%BB%9F%E8%AE%A1%E4%BF%A1%E6%81%AF


site:en.wikipedia.org

Google 找到约 14,100,000 条结果 （用时 0.28 秒）
Baidu 找到相关结果数23,200,000个。

Pages
(All pages in the wiki, including talk pages, redirects, etc.)	32,489,471

Content pages	4,476,861


关于已抓取到的数据，为了保证多线程下统计数据的正确，参考http://stackoverflow.com/questions/10778493/whats-the-diff-between-findandmodify-and-update-in-mongodb
实现安全的自增

