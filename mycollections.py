
# coding:utf-8


# 自定义tuple对象
from collections import namedtuple

# namedtuple('名称', [属性list]):
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x, p.y

print isinstance(p, Point)
print isinstance(p, tuple)

# 圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.appendleft('L')
q.append('R')
print q
l = q.popleft()
print q

# 可以设置默认值的Dict
from collections import defaultdict
dd = defaultdict(lambda: None)
dd['key1'] = 'val1'
print dd['key1']
print dd['key2']

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
# dict的Key是无序的
print d

print d.has_key('a')
print 'a' in d

for value in d:
    print value

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# OrderedDict的Key是有序的 ,为插入的顺序
print od


from collections import OrderedDict

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print c
