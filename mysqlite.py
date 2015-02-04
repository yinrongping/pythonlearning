#!/usr/bin/python
# coding:utf-8
import sqlite3
import mysql.connector

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute(
# 'create table user(id varchar(20) primary key,name varchar(20))')
# cursor.execute('insert into user (id,name) values(\'2\',\'Roy.yin\')')
# print cursor.rowcount
# cursor.close()

# cursor2 = conn.cursor()
# cursor2.execute('select * from user where id=? or id = ?', ('1', '2'))
# 返回的是一个list,里面的元素是tuple
# values = cursor2.fetchall()
# print values
# cursor2.close()
# conn.commit()
# conn.close()


conn = mysql.connector.connect(
    user='root', password='root', database='test', use_unicode=True)
# cursor = conn.cursor()
# cursor.execute(
#     'create table user(id varchar(20) primary key,name varchar(20))')
# cursor.execute('insert into user (id,name) values(\'1\',\'Roy.yin\')')
# print cursor.rowcount
# cursor.close()

cursor2 = conn.cursor()

cursor2.execute('select id,name from user where id = %s' % '1')
for x in cursor2.description:
    print x
# 返回的是一个list,里面的元素是tuple
values = cursor2.fetchall()
print values
cursor2.close()
conn.commit()
conn.close()
