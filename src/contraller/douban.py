#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangyl96@foxmail.com
@software: garner
@file: douban.py
@time: 2018/11/12 16:12
@desc: 豆瓣爬取调度中心
'''
from src.logical.db.DB import DB
from src.util.config_util import PropertiesUtil
from src.logical.crawl.doubanCrawl import DoubanCrawl
from src.logical.extract.doubanExtract import DoubanExtract

# property = PropertiesUtil()
# cachePath = property.prop("cache_path")
# baseUrl = property.prop("world_famous_books_url")
#
# doubanCrawl = DoubanCrawl(baseUrl, cachePath)
# result = doubanCrawl.crawl()
# doubanExtract = DoubanExtract()
# bookStore = []
# for i in range(1):
#     html = str(result[i], encoding="utf-8")
#     bookStore = bookStore + doubanExtract.extract(html)
#
# print(len(bookStore))


class DoubanBook(object):
    def __init__(self, configPath=None):
        self.config = PropertiesUtil(configPath)
        self.crawl = DoubanCrawl(self.config.prop("world_famous_books_url"), self.config.prop("cache_path"))
        self.extract = DoubanExtract()
        self.db = DB(passwd=self.config.prop('db_passwd'), db=self.config.prop('db_schema'))

    def crawler(self, page=0):
        return self.crawl.crawl(page)

    def extractor(self, html):
        return self.extract.extract(html)

    def writer(self, book):
        self.db.insert(book.insert())
        print("INSERT", book.getTitle())

    def __call__(self):
        count = 0
        try:
            for page in range(54, 78):
                pageHtml = self.crawler(page)
                bookList = self.extractor(str(pageHtml, encoding="utf-8"))
                count = count + len(bookList)
                for book in bookList:
                    self.writer(book)
        except Exception as e:
            print(str(e))
        finally:
            self.db.close()
        print(str(count))