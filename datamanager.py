#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import psycopg2

"""
使用mongodb来存储数据
使用pg来维护已经爬取的表
"""
__all__ = ['writer', 'manager', 'get_url']

host = '127.0.0.1'
client = MongoClient(host, 27017)
db = client.history_people
db.authenticate("root", "passward")
collection = db.people

database = 'people'
user = 'postgres'
port = 5432
password = 'passward'


def writer(content: dict):
    if content is not None:
        collection.insert_one(content)


def manager(urls: dict, batch: int) -> None:
    conn = psycopg2.connect(database=database, host=host,
                            port=port, user=user, password=password)
    cur = conn.cursor()
    for key in urls.keys():
        cur.execute("INSERT INTO people(url, title, batch) VALUES(%s,%s,%s) ON conflict(url) DO NOTHING", (urls[key], key, batch))
    conn.commit()
    cur.close()
    conn.close()


def get_url(batch: int) -> tuple:
    conn = psycopg2.connect(database=database, host=host,
                            port=port, user=user, password=password)
    cur = conn.cursor()
    cur.execute("SELECT url FROM people WHERE batch=%s", str(batch))
    url_new = cur.fetchall()
    cur.close()
    conn.close()

    return url_new


if __name__ == "__main__":
    manager({'诸葛亮': 'https://baike.baidu.com/item/%E8%AF%B8%E8%91%9B%E4%BA%AE/21048'})
