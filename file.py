#!/usr/bin/python
# coding:utf-8

# f = open('d:/python/user.py', 'r')
# print f.read()
# f.close()

# 第一种写法
# try:
#     f = open('d:/python/user.py', 'r')
#     print f.read()
# finally:
#     if f:
#         f.close()

# 第二种写法 用 with 更加简洁
# 不需要close() with 自动帮我们调用close()方法
# with open('d:/python/user.py', 'r') as f:
#     for line in f.readlines():
#         print line.strip()

# file 写入
# with open('d:/python/user.py', 'w') as f:
# f.write('# 222222加入')

import os

print os.name


# print os.uname() windows 不提供此方法

# 环境变量
print os.environ

# 获取某个环境变量值
print os.getenv('PATH')


# 查看当前目录的绝对路径
print os.path.abspath('.')

# 新建文件夹，先获取路径
#path = os.path.join(os.path.abspath('.'), 'testdir')
# os.mkdir(path)
# 删除文件夹
# os.rmdir(path)


# print[x for x in os.listdir('.') if os.path.isfile(x) and
# os.path.splitext(x)[1] == '.txt']

def search(dir, file):
    for f in os.listdir(dir):
        fpath = os.path.join(dir, f)
        if os.path.isfile(fpath):
            if os.path.split(fpath)[1] == file:
                print fpath
        else:
            if os.path.isdir(fpath):
                search(fpath, file)

search(os.path.abspath('.'), '2.py')


# 对象的序列号
try:
    import cPickle as pickle
except ImportError:
    import pickle

#
d = {'name': 'Roy', 'age': 20, 'addr': '上海市普陀区'}

print d

# 将对象序列化
print pickle.dumps(d)

# 将对象序列化 并保存到文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 读取序列化文件 转化为实体
f2 = open('dump.txt', 'rb')
d2 = pickle.load(f2)
f.close()
print d2

# Dict 转化为json
import json
d = {'name': 'Roy', 'age': 20, 'addr': 'shanghai city'}
print json.dumps(d)

# 将json反转为对象：反序列化得到的所有字符串对象默认都是unicode而不是str
jsonstr = '{"age": 20, "name": "Roy", "addr": "shanghai city"}'
dic = json.loads(jsonstr)
print dic


# class对象转json
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# 需要定义一个转化函数


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print s.__dict__
# print(json.dumps(s)) #报错
# 转化成功
print(json.dumps(s, default=student2dict))
# 使用 default=lambda obj: obj.__dict__ 适用所有对象
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

# 将json反转为class对象
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
