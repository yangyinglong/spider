#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangyl96@foxmail.com
@software: garner
@file: application.py
@time: 2018/11/15 11:48
@desc:
'''
from src.contraller.douban import DoubanBook

if __name__ == "__main__":
    douban = DoubanBook("setting/config")
    douban()