#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 多进程和多线程
# import os
# from multiprocessing import Process

from multiprocessing import Pool
import os
import time
import random

print 'Process-%s is starting ...' % os.getpid()
# windows 没有fork
pid = os.fork()
if pid == 0:
    print 'this is child process-%s and parent process is %s.' % (os.getpid(), os.getppid())
else:
    print 'I %d just create a child process-%s.' % (os.getpid(), pid)


from multiprocessing import Process
import os

# 子进程要执行的代码


def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    print 'Process end.'


# 线程池Pool
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


print 'Parent process %s.' % os.getpid()
p = Pool()
for i in range(5):
    p.apply_async(long_time_task, args=(i,))
print 'Waiting for all subprocesses done...'
p.close()
p.join()
print 'All subprocesses done.'


# 进程间通信
from multiprocessing import Process, Queue

# 写数据进程执行的代码:


def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:


def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
