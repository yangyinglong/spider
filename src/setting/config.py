#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangyl96@foxmail.com
@software: garner
@file: config.py
@time: 2018/11/12 16:00
@desc: 配置类
'''

class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class PublicConfig:
    HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
    # 网站接口
    CHROME_URL = "https://suiyijie.fanzhoutech.com/admin/applyform/applybilllist"
    APPLY_URL = "https://suiyijie.fanzhoutech.com/admin/applyform/applybilllist"
    REPAYMENTS_URL = "https://suiyijie.fanzhoutech.com/admin/applyform/repaymentslist"
    PERSON_URL = "https://suiyijie.fanzhoutech.com/admin/applyform/auditinfo/"
    PERSON_MAIL_URL = "https://suiyijie.fanzhoutech.com"

class DevelopmentConfig(Config):
    DEBUG = True
    # 文件存储地址

class TestingConfig(Config):
    TESTING = True
    # 文件存储地址


class ProductionConfig(Config):
    None
    # 文件存储地址


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
