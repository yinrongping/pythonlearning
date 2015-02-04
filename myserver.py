#!/usr/bin/python
# coding:utf-8

# WSGI：Web Server Gateway Interface
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

# 我们自己编写的application函数


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')


# 创建一个服务器，IP地址为空，端口是8001，处理函数是application:
httpd = make_server('', 8001, application)
print "Serving HTTP on port 8000..."
# 开始监听HTTP请求:
httpd.serve_forever()
