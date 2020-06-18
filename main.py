#!/usr/bin/env python
# -*- coding:utf-8 -*-
from downloader import *
from htmlparser import *
from datamanager import *

"""
主程序
"""
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
url_list = get_url(0)

print('start')
i = 1
while url_list:
    for url in url_list:
        print(url)
        response = downloader(url=url[0], header=header)
        content, urls = parser(response=response)
        print(len(urls))
        if content is not None:
            content['url'] = url[0]
            writer(content)
        manager(urls, i)
    url_list = get_url(i)
    i += 1
