#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangyl96@foxmail.com
@software: garner
@file: book.py
@time: 2018/11/13 10:23
@desc:print(code, " ", title, " ", subtitle, " ", price1, " ", price2, " ", price3,
                  " ", author, " ", translator, " ", label, " ", average, " ", ratingsNum,
                  " ", describe, " ", imgUrl)
'''

class Book(object):
    def __init__(self, title, code, subtitle, price1, price2, price3,
                   author, translator, label, average, ratingsNum,
                   describe, imgUrl, kind="未知"):
        self.id = code,
        self.id = list(self.id)[0]      # id 自动变成了 tuple ，所以这一行是用来转类型
        self.title = title
        self.subtitle = subtitle
        self.price1 = price1
        self.price2 = price2
        self.price3 = price3
        self.author = author
        self.translator = translator
        self.label = label
        self.average = average
        self.ratingsNum = ratingsNum
        self.describe = describe
        self.imgUrl = imgUrl
        self.kind = kind

    def print(self):
        print(self.id, " ", self.title, " ", self.subtitle, " ", self.price1, " ", self.price2, " ", self.price3,
              " ", self.author, " ", self.translator, " ", self.label, " ", self.average, " ", self.ratingsNum,
              " ", self.describe, " ", self.imgUrl)

    def getTitle(self):
        return self.title

    def insert(self):
        insertSql = "insert into book_store set code = '" + self.id + "', title = \"" + self.title + "\""
        if self.subtitle != None:
            insertSql = insertSql + ", subtitle = '" + self.subtitle + "'"
        if self.price1 != None:
            insertSql = insertSql + ", price1 = '" + self.price1 + "'"
        else:
            insertSql = insertSql + ", price2 = '" + self.price2 + "', price3 = '" + self.price3 + "'"
        insertSql = insertSql + ", author = '" + self.author + "'"
        if self.translator != None:
            insertSql = insertSql + ", translator = '" + self.translator + "'"
        insertSql = insertSql + ", label = '" + self.label + "'"
        if self.average != None:
            insertSql = insertSql + ", average = " + self.average
        if self.ratingsNum != None:
            insertSql = insertSql + ", ratings_num = " + self.ratingsNum
        insertSql = insertSql + ", describes = \"" + self.describe + "\", img_url = '" + self.imgUrl + "', kind = '" +\
                    self.kind + "';"
        return insertSql
