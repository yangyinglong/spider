#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangyl96@foxmail.com
@software: garner
@file: down_util.py
@time: 2018/11/12 10:42
@desc: 根据 url 下载页面信息
'''

from datetime import datetime
from urllib.request import Request, build_opener, ProxyHandler
from urllib.parse import urlparse
import random
import socket

# from save_util import DiskCache

DEFAULT_AGENT = 'wswp'
DEFAULT_DELAY = 5
DEFAULT_RETRIES = 1
DEFAULT_TIMEOUT = 60


class Throttle:
    """控制同一个页面的访问频率"""
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() -
				last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()

class Downloader:
    def __init__(self, delay=DEFAULT_DELAY, user_agent=DEFAULT_AGENT, proxies=None, num_retries=DEFAULT_RETRIES, timeout=DEFAULT_TIMEOUT, opener=None, cache=None):
        socket.setdefaulttimeout(timeout)
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.opener = opener
        self.cache = cache

    def __call__(self, url, data=None):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
            else:
                if result['code'] == None or self.num_retries > 0 and 500 <= result['code'] < 600:
                    result = None
        if result is None:
            self.throttle.wait(url)
            proxy = random.choice(self.proxies) if self.proxies else None
            headers = {'User-agent': self.user_agent}
            result = self.download(url, headers, proxy, self.num_retries, data)
            if self.cache:
                self.cache[url] = result
        return result['html']

    def download(self, url, headers, proxy, num_retrie, data = None):
        print('Download:' + url)
        request = Request(url, data, headers or {})
        opener = self.opener or build_opener()
        if proxy:
            proxy_params = {urlparse(url).scheme: proxy}
            opener.add_handler(ProxyHandler(proxy_params))
        try:
            response = opener.open(request)
            html = response.read()
            code = response.code
        except Exception as e:
            print('Download error', str(e))
            html = ''
            if hasattr(e, 'code'):
                code = e.code
                if num_retrie > 0 and 500 <= code < 600:
                    return _get(url, headers, proxy, num_retrie-1, data)
            else:
                code = None
        return {'html': html, 'code': code}

if __name__ == "__main__":
    down = Downloader(cache=DiskCache('../output'))
    result = down('http://www.baidu.com')