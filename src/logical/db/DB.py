#!/usr/bin/env python
# encoding: utf-8
'''
@author: yangyinglong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: yangyl96@foxmail.com
@software: garner
@file: DB.py
@time: 2018/11/14 18:15
@desc:
'''
import time
import pymysql

class DB(object):
    def __init__(self, host='127.0.0.1', port=3306, user='root', passwd='root', db='suiyijie'):
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        print("=======>>> DB connect success  <<<========")
        self.failSqlLog = open("../output/log/failSql.txt", 'a', encoding='utf-8')
        self.successSqlLog = open("../output/log/successSql.txt", 'a', encoding='utf-8')

    def insert(self, sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            self.successSqlLog.writelines(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + " : " +
                                          sql + "\n")
        except Exception as e:
            self.failSqlLog.writelines(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + " : ")
            self.failSqlLog.writelines(sql + "\n")
            self.failSqlLog.writelines(str(e) + "\n")

    def close(self):
        self.conn.close()
        print("=======>>> DB close success  <<<========")
        self.failSqlLog.close()
        self.successSqlLog.close()


