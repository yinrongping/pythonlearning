#!/usr/bin/env python
# -*-coding:utf-8-*-
import anydbm
import shelve

'''
anydbm允许我们将一个磁盘上的文件与一个“dict-like”对象关联起来，
操作这个“dict-like”对象，就像操作dict对象一样，最后可以将“dict-like”的数据持久化到文件
anydbm.open(filename[, flag[, mode]])，filename是关联的文件路径，
可选参数flag可以是: 'r': 只读, 'w': 可读写, 'c': 如果数据文件不存在，
就创建，允许读写; 'n': 每次调用open()都重新创建一个空的文件
'''


def createdb():
    try:
        # key和value的类型必须是字符串
        db = anydbm.open('db.bat', 'c')
        db['string1'] = 'hello'
        db['key'] = 'value'
    except Exception, e:
        raise e
    else:
        pass
    finally:
        db.close()


def loaddb():
    try:
        db = anydbm.open('db.bat', 'r')
        for item in db.items():
            print item
    except Exception, e:
        raise e
    else:
        pass
    finally:
        db.close

'''
shelve模块是anydbm的增强版，它支持在"dict-like"对象中存储任何可以被pickle序列化的对象，但key也必须是字符串
'''


def createdb2():
    try:
        # key必须是字符串,value可以是任何可以被pickle序列化的对象
        db = shelve.open('db2.bat', 'c')
        db['int'] = 100
        db['String'] = 'hello world'
        db['tunpl'] = (1, 2, 3)
    finally:
        db.close()


def loaddb2():
    try:
        db = shelve.open('db2.bat', 'r')
        for item in db.items():
            print item
    except Exception, e:
        raise e
    finally:
        db.close()

if __name__ == '__main__':
    createdb()
    loaddb()
    createdb2()
    loaddb2()
