#!/usr/bin/env python
# coding:utf-8

import itertools
from itertools import chain
from itertools import groupby

# 无限数字迭代器
natuals = itertools.count(1)

for n in natuals:
    print n
    if n == 10:
        break

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n


# 无限循环 迭代器
cs = itertools.cycle('ABC')
for c in cs:
    print c
    if c == 'C':
        break

# 设置重复次数
ns = itertools.repeat('A', 10)
for n in ns:
    print n

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for ch in chain('xyz', 'abc'):
    print ch

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in groupby('AAABBBCCAAA'):
    print key, list(group)

for key, group in groupby('AaaBBbCcAaA', lambda c: c.upper()):
    print key, list(group)

# imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x

r = map(lambda x: x * x, [1, 2, 3])
print r
