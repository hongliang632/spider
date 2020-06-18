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