#!/usr/bin/python
# coding:utf-8

import copy
import math
import logging
from types import MethodType


logging.basicConfig(level=logging.INFO)

print 'hello,world', '中文'
print 'The quick brown fox', 'jumps22 over', 'the lazy dog'
print "Hello world!"
print 100 + 200
print 'your name:%s,your age:%d' % ('many', 100)

# List 集合2
students = ['lucy', 'nadan', 'royin']
teacher = 1, 2, 1, 4
print teacher[1]
print students
print len(students)
print students[2]
print students
print students[-1]
print students[-2]
print students[-0]
# List 新增
students.append('meiyi')
print students[-1]
# List 删除
popval = students.pop()
print popval
popval = students.pop(-2)
print popval
students[1] = 'Nana'
print students
# 2维数组
arr = ['1', '2', ['11', '12'], '3']
print arr[2][0]
print 'this string to int :', int(arr[2][0])
tuparr = (1, 2, 3, ['41', '42'], 5)
print tuparr[3][1]
# tuparr[2] = 'a' //无法改变值2
tuparr[3][0] = 12
print tuparr
2


# del 删除元素
members = [1, 2, 3, 4]
print members
del members[1]
print members

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

#
arr3 = arr1 + arr2

# 元素扩展 新增
arr1.extend(arr2)

print arr1
# 弹出最后一个 删除
arr2.pop()

print arr2
# 列表元素重复次数
print arr1 * 3


# 条件判断和循环
age = 20
if age > 20:
    print 'age > 20'
elif age == 20:
    print 'age = 20'
else:
    print 'age < 20'

x = True
if x:
    print 'this is Ture'
for name in students:
    print name

for i in [1, 2, 3, 6]:
    print i
for x in range(10):
    print 'range:', x

# dict
d = {'User1': 1, 'User2': 2, 'User3': 3, 'User4': 0, 'User4': 7}
print d
print d['User2']
d['User3'] = 'aaa'
print d
# print d['User4'] //key不存在报错
print d.get('User1')
print d.get('User10')  # key不存在返回none
# 删除key
dval = d.pop('User1')
print dval
ditems = d.items()
for(k, v) in ditems:
    print 'key:', k, ',value:', v
# if d.has_key('User2'):  # //老版本2.2之前
#	print 'd has User2'
if 'User3' in d:
    print 'd has User3'
# 获取不到指定返回值
print d.get('User10', -1)
# Dict 修改和新增
dic = {"a": "apple", "b": "banana"}
print dic
dict2 = {"c": "grape", "d": "orange"}
dic.update(dict2)
print dic
dic.update({"e": "fff"})
print '--------------', dic

print dic.keys()
print dic.values()
print dic.items()
print dic.get('add', 'b')
dic['e'] = 'pig'
print dic

dic = {"a": "apple", "b": {"g": "grape2", "o": "orange"}}
dict2 = copy.deepcopy(dic)
print dict2
dict3 = copy.copy(dic)
print dict3
dict222 = dict()
d = dict(name='visaya', age=20)
d = dict(zip(['name', 'age', 'sex'], ['visaya', 20, 1]))
print d
dict4 = dict2.fromkeys(['a', 'b'], 1)
print dict4

print 212

# Set

s = set([1, 2, 3])
s.add(3)
s.add(4)
s.update([1, 2, 5])
s.remove(2)
print s
a = ['c', 'b', 'a']
a.sort()
print a
a = cmp(1, 4)
print a


def my_add(x, y):
    return x + y

val = my_add(2, 4)
print val

a = cmp
val = a(12, 2)
print val


def return_more(x, y):
    return x, y
x, y = return_more(100, '知道')
print x
print y


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
r, u = move(100, 100, 60)
print r, u


def power(x, n=2):
    s = 1
    while n > 0:
        s = x * s
        n = n - 1
    return s

print power(5, 2)
# Error
# print power(5, '2')

# 关键字参数


def person(name, age, **kw):
    return 'name:', name, 'age:', age, "other:", kw
print person('Roy', 20)
print person('Roy', 20, gener='M', job='engineer')

# 参数组合


def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

name = '1,2,3,4,5'
print name[1]
tup = tuple(s)
print tup[1], tup[0], tup[2]


# 动态的赋值方法
class Student(object):
    # 允许的绑定字段名
    __slots__ = ('age', 'score', 'name', 'print_age')

    def __init__(self, name, score):
        self.name = name
        self.score = score


s = Student("zhangsan", 100)

print s.name


def print_age(self, age):
    self.age = age

# 绑定方法到某个实例
s.print_age = MethodType(print_age, s, Student)

# 绑定方法到对象
# s.print_age = MethodType(print_age, None, Student)

s.print_age(25)

print s.age


# 属性注解 设置getter and setter
class Teacher(object):

    @property
    def score(self):
        print 'get score...'
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be int!')
        elif score < 0 or score > 100:
            raise ValueError('score much between 0 ~ 100!')
        self._score = score
        print 'set score...'
t = Teacher()
t.score = 100
print t.score

# **表示几的几次方
print 5 ** 2

# 3.0以上版本 // 表示地板除,/ 普通除法，5/2 = 2.5
print 5 // 2

# 'r'可以防止字符串特殊的转移
print r'nihao \new'

# map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  已后面的为参数 循环执行fn

# sorted([36, 5, 12, 9, 21]) 排序
# sorted([36, 5, 12, 9, 21], reversed_cmp)自定义排序规则
# map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]) lambda表示匿名函数
# 偏函数 functools.partial可以固定参数


#__str__ 方法 print 实例的时候执行
#__repr__ 方法 执行打印实例的时候执行

#__iter__ 使类可以循环 next 获取值 遇到StopIteration停止
class Fib(object):

    """docstring for Fib"""
    type = 'FibType'

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        while self.a > 100:
            raise StopIteration
        return self.a

    # def __getitem__(self, n):
    #     a, b = 1, 1
    #     for x in range(n):
    #         a, b = b, a + b
    #     return a

    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n, int):
            for x in range(n):
                a, b = b, a + b
            return a
        L = []
        if isinstance(n, slice):
            for x in range(n.stop):
                if x >= n.start:
                    L.append(a)
                a, b = b, a + b
            return L

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError('\'Fib\' has no attr with \'%s\'' % attr)

    def __call__(self):
        print('This is Fib instance!')

for obj in Fib():
    print obj

# __getitem__ 可以使对象使用索引
print Fib()[4]
print Fib()[10]

#__getitem__ 支持slice切片需要改写
print Fib()[2:6]

# __getattr__
s = Fib()
# return 99
print s.score

#'Fib' has no attr with 'name'
# print s.name

s.name = 'Roy'
print s.name

# __call__ 使实例本身可以被调用
s()
print callable(Fib)  # True 可以被调用

# FibType 类的属性，
print Fib.type  # FibType
print s.type  # FibType
s.type = 'sFibtype'  # sFibtype 类属性被实例的属性覆盖了
print s.type

# type() 用于动态的创建类对象


def sayHello(self, name):
    print('sayHello to %s...' % name)


def sayBye(self, name):
    print('sayBye to %s...' % name)
# 类名称  , 继承的分类（注意使用tuple），绑定方法
Hello = type('Hello', (object,), dict(sayHello=sayHello, sayBye=sayBye))

h = Hello()
h.sayHello('Roy')
h.sayBye('lucy')

# Python 异常处理  assert 断言，不成立执行后面 logging 打印日志
try:
    print 'try...'
    n = 1
    #assert n != 1, 'n ==1'
    logging.info('this is logging print...')
    s = 10 / 0
    print s
except ZeroDivisionError, e:
    print 'except', e
else:  # 没有异常是执行
    print 'no error...'
finally:
    print 'finally...'

s = r'ABC\-001'  # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'
print s

# 正则匹配 成功返回Match 对象 否则None
import re
print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# 分割字符串
print re.split(r'\s+', 'a b   c')

# 正则匹配分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0)
print m.group(1)
print m.group(2)

# 默认正则是贪婪匹配
print re.match(r'^(\d+)(0*)$', '102300').groups()
# 增加？，改为非贪婪匹配
print re.match(r'^(\d+?)(0*)$', '102300').groups()

s3 = '''hello,# nihao a
world,
hahaha.'''
print s3
