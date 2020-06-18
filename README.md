# 百度百科人物简介和标签爬虫

## 依赖
requests==2.23.0
pymongo==3.10.1
psycopg2==2.8.4
beautifulsoup4==4.9.1

## 结构
```
├──datamanager.py      数据管理:将数据写入到数据库之中；
├──downloader.py       下载页面；
├──htmlparser.py       页面解析:爬取相应位置的数据；
├──main.py             主程序
├──names.txt           人名词典    
```

任务是爬取百度百科的人物词条，但是由于难以判断词条是不是人物。所以这里使用了一份人名词典。

使用postgres存储已经爬取的链接，使用mongodb存储爬取的数据。

代码详细说明看[个人博客](https://www.hongkg.cn/2020/06/18/%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91%E8%AF%8D%E6%9D%A1%E7%88%AC%E8%99%AB/#more)
