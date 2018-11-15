#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangyl96@foxmail.com
@software: garner
@file: config_util.py
@time: 2018/11/12 15:29
@desc: 从 setting/config.txt 中读取配置
'''

class PropertiesUtil(object):
    def __init__(self, configPath="../setting/config"):
        self.path = configPath
        self.config = {}
        with open(self.path, 'r') as fp:
            allConfig = fp.readlines()
            for one in allConfig:
                if one.startswith("#") or one == '\n' or "=" not in one:
                    continue
                kv = one.replace(" ", "").replace("\n", "").split("=")
                try:
                    self.config[kv[0]] = kv[1]
                except:
                    None

    def prop(self, key):
        try:
            return self.config[key]
        except:
            return None

if __name__ == "__main__":
    url = PropertiesUtil().prop("base_url")
    print(url)