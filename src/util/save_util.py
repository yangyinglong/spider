#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: save_util.py
@time: 2018/11/12 9:59
@desc: 根据 url 保存页面信息到本地或者数据库中
'''

from datetime import timedelta,datetime
# from pymongo import MongoClient
from urllib.parse import urlparse,urlsplit

import os
import pickle
import re


class DiskCache(object):
    """docstring for DiskCache"""
    def __init__(self, cache_dir='cache', expires=timedelta(days=30)):
        self.cache_dir = cache_dir
        self.expires = expires

    def url_to_path(self, url):
        components = urlsplit(url)
        path = components.path
        if not path:
            path = '/index.html'
        elif path.endswith('/'):
            path = path + '/index.html'
        filename = components.netloc + path + components.query
        filename = re.sub('[^/0-9a-zA-Z\-.,;_]', '_', filename)
        filename = '/'.join(segment[:255] for segment in filename.split('/'))
        return os.path.join(self.cache_dir, filename)

    def __getitem__(self, url):
        path = self.url_to_path(url)
        if os.path.exists(path):
            with open(path, 'rb') as fp:
                result, timestamp = pickle.load(fp)
                if self.has_expired(timestamp):
                    print(url + ' has expires')
                    raise KeyError(url + ' has expires')
                return result
        else:
            raise KeyError(url + ' does not exist')

    def __setitem__(self, url, result):
        path = self.url_to_path(url)
        folder = os.path.dirname(path)
        timestamp = datetime.utcnow()
        data = pickle.dumps((result, timestamp))
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(path, 'wb') as fp:
            fp.write(data)

    def has_expired(self, timestamp):
        return datetime.utcnow() > timestamp + self.expires


class MongoCache(object):
    def __init__(self, client=None, expires=timedelta(days=30)):
        self.client = MongoClient('127.0.0.1', 27017) if client is None else client
        self.db = self.client.cache
        self.db.webpage.create_index('timestamp', expireAfterSeconds=expires.total_seconds())

    def __getitem__(self, url):
        record = self.db.webpage.find_one({'_id': url})
        if record:
            return record['result']
        else:
            raise KeyError(url + ' does not exist')

    def __setitem__(self, url, result):
        record = {'result': result, 'timestamp': datetime.utcnow()}
        self.db.webpage.update({'_id': url}, {'$set': record}, upsert=True)


if __name__ == "__main__":
    # diskCache = DiskCache('../output')
    # diskCache.__setitem__('http://www.baidu.com/index.html;user?id=5#comment', 'aaaaaaaaaaaaa')
    # result = diskCache.__getitem__('http://www.baidu.com/index.html;user?id=5#comment')
    # print(result)
    # timestamp = datetime.utcnow()
    # timestamp = bytes(str(timestamp), encoding="utf-8")
    # with open ('time.txt', 'wb') as fp:
    #     fp.write(timestamp)
    sql = "insert into xxx set a = %d" % (1)
    print(sql)
