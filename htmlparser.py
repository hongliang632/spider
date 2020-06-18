#!/usr/bin/env python
# -*- coding:utf-8 -*-
import bs4
import re
import sys
import io

"""
从网页中获取新的链接和网页内容
"""

__all__ = ['parser']

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

names = set()

with open('names.txt', 'r', encoding='utf-8-sig') as file:
    for line in file.readlines():
        line = line.strip()
        names.add(line)


def is_people_name(name):
    if name in names:
        return True
    else:
        return False


def get_new_url(page) -> dict:
    links = page.find_all('a', target='_blank', href=re.compile("/item/*"))
    new_url = {}
    words = ['达人', '秒懂', '本人', '义项', '义词', '百科', '\n', ' ']
    for link in links:
        name = link.get_text()
        url = link["href"]
        flag = True
        for word in words:
            if word in name:
                flag = False
        if name not in new_url and name != '' and flag and is_people_name(name):
            new_url[name] = 'https://baike.baidu.com' + url
    return new_url


def get_new_content(page) -> dict:
    new_content = {}
    try:
        # 如果是爬取正文，可以使用 {"class": re.compile("para(-title)*"),"label-module": re.compile("para(-title)*")}
        # 爬取简介内容
        title = page.find("h1").get_text()
        subtitle = page.find("h2").get_text()
        new_content['title'] = title
        new_content['complete_title'] = title + subtitle
        para = page.find("div", {"class": "lemma-summary", "label-module": "lemmaSummary"})
        introduction = para.get_text()
        introduction = re.sub('\\[.*?]|\xa0|\n', '', introduction)
        new_content['introduction'] = introduction

        items = page.find("div", {"class": "basic-info cmn-clearfix"})
        names = items.findAll("dt", {"class": "basicInfo-item name"})
        values = items.findAll("dd", {"class": "basicInfo-item value"})
        for name, value in zip(names, values):
            name = name.get_text()
            name = re.sub('\\[.*?]|\xa0|\n', '', name)
            value = value.get_text()
            value = re.sub('\\[.*?]|\xa0|\n', '', value)
            new_content[name] = value
        return new_content

    except AttributeError as e:
        return None


def parser(response) -> tuple:
    if response is not None:
        page = bs4.BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
        content = get_new_content(page)
        url = get_new_url(page)
        return content, url
    else:
        return None, None
