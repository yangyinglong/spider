#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangyl96@foxmail.com
@software: garner
@file: doubanCrawl.py
@time: 2018/11/12 17:38
@desc:  爬取数据
'''

from src.util.down_util import Downloader
from src.util.save_util import DiskCache

class DoubanCrawl(object):
    def __init__(self, baseUrl, cachePath):
        self.baseUrl = baseUrl
        self.down = Downloader(cache=DiskCache(cachePath))

    def crawl(self, page):
        url = self.baseUrl + "?start=%d&sort=hot&promotion_only=False&min_price=None&max_price=None&works_type=None" % (page*20)
        return self.down(url)