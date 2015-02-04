#!/usr/bin/python
# coding:utf-8
# print user
import time
import datetime

# 字典的更新
dict1 = {"a": "apple", "b": "banana"}
print dict1
dict2 = {"a": "grape", "d": "orange"}
dict1.update(dict2)
print dict1

a = 3


def pf():
    global a
    a = 10
    print a
pf()
print a

u1 = [(1, 2), (3, 4), (5, 6)]
u2 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

#cols, args = zip(*u1)
print u2.iteritems()

cols, args = zip(*u2.iteritems())
print cols
print args


u3 = dict(id2=100, name2='Alice', email2='alice@test.org')

cols, vals = zip(*u3.iteritems())

print cols
print vals

_triggers = frozenset(('a', 'v', 'w', 'f'))
print _triggers

vvv = False

print 'a', (vvv and 'b' or 'c')

print datetime.datetime.now()  # 2014-12-23 17:48:01.777000
day1 = datetime.datetime(2005, 2, 16)  # 2005-02-16 00:00:00
print day1
day2 = datetime.timedelta(days=10)  # 10 days, 0:00:00
# time.ctime([sec])#把秒数转换成日期格式，如果不带参数，则显示当前的时间
print time.ctime()
print day1 - day2  # 2005-02-06 00:00:00 10天前的日期
print day1.ctime()  # Wed Feb 16 00:00:00 2005
print datetime.datetime.now().time()  # 取得当前时间 17:51:44.099000
# date->string类型
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
print time.strptime('2014-12-23 17:59:48', '%Y-%m-%d %H:%M:%S')
