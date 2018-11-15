#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangyl96@foxmail.com
@software: garner
@file: doubanExtract.py
@time: 2018/11/12 17:54
@desc: 解析爬取到的数据
'''

from bs4 import BeautifulSoup
from src.dao.book import Book

class DoubanExtract(object):
    def __init__(self):
        None
        # 定义一些规则

    def extract(self, html):
        soup = BeautifulSoup(html, "html.parser")
        eBookList = soup.select('li[class="item store-item"]')
        bookStore = []
        for eBook in eBookList:
            title = eBook.select('div[class="title"]')[0].a.text
            try:
                subtitle = eBook.select('div[class="title"]')[0].p.text
            except:
                subtitle = None
            code = eBook.a['href'].split("/")[2]
            price1Element = eBook.select('span[class="price-tag "]')
            price1 = None
            price2 = None
            price3 = None
            if price1Element:
                price1 = price1Element[0].text.replace("元", "")
            else:
                price2Element = eBook.select('s[class="original-tag"]')
                price2 = price2Element[0].text.replace("元", "")
                price3Element = eBook.select('span[class="discount-price"]')
                price3 = price3Element[0].text.replace("元", "")
            authorElements = eBook.select('a[class="author-item"]')
            author = authorElements[0].text
            if len(authorElements) > 1:
                translator = authorElements[1].text
            else:
                translator = None
            label = eBook.select('span[itemprop="genre"]')[0].text
            try:
                average =eBook.select('span[class="rating-average"]')[0].text
            except:
                average = None
            try:
                ratingsNum = eBook.select('a[class="ratings-link"]')[0].text.replace("人评价", "")
            except:
                ratingsNum = None
            describe = eBook.select('div[class="article-desc-brief"]')[0].text.replace("\"", "")
            imgUrl = eBook.a.img['src']
            book = Book(title, code, subtitle, price1, price2, price3,
                   author, translator, label, average, ratingsNum,
                   describe, imgUrl, "推理悬疑")
            bookStore.append(book)
        return bookStore
