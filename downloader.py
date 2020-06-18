#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib.request
from urllib.error import HTTPError, URLError
import requests

__all__ = ['downloader']


def downloader(url: str, header: dict):
    try:
        # 使用requests也是一样的
        # response = requests.get(url, headers=header)
        # response.encoding = "utf-8"
        request = urllib.request.Request(url, headers=header)
        response = urllib.request.urlopen(request)
        return response
    except (HTTPError, URLError) as e:
        return None
