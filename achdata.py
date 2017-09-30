#!/usr/bin/env python
# coding=utf-8

import pymysql as pm
import random
config = {
    'host': '10.130.2.178',
    'port': 3306,
    'user': 'root',
    'passwd': '910830gz',
    'db': 'ach',
    'charset': 'utf8'
}


def getID(cont):
    conn = pm.connect(**config)
    with conn:
        cur = conn.cursor()
        cur.execute("select id from project where content like '%s'" % cont)
        #此处的 /s 必须加引号,否则报错
        return cur.fetchone()


def getResultFromDB(table, num=None):
    conn = pm.connect(**config)
    with conn:
        cur = conn.cursor()
        if num == None:
            count = cur.execute("select id from %s" % table)
            num = random.randint(1, count)
        if table == 'project':
            cur.execute(
                "select tasktype, content, object from project where id = %d" % num)
        else:
            cur.execute("select result from results where id = %d" % num)
        result = cur.fetchone()
        return result


if __name__ == '__main__':

    for x in getResultFromDB('project'):
        print x
