#!/usr/bin/env python
# coding=utf-8

import pymysql
import settings


class MySQL(object):

    def __init__(self, host=settings.MYSQL_HOST, port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER, password=settings.MYSQL_PASSWORD,
            database=settings.MYSQL_DATABASE):
        try:
            self.db = pymysql.connect(host, user, password, 
                    database, charset='utf-8', port=port)
            self.cursor = self.db.cursor
        except pymysql.MySQLError as e:
            print (e.args)

    def insert(self, table='article', data: dict):
        '''
        想数据库插入文章
        '''
        args = ','.join(data.keys())
        values = ','.join(['%s']*len(data))
        sql = 'insert into %s (%s) values(%s)' % (table, args, values)
        try:
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            print (e.args)
            self.db.rollback()

