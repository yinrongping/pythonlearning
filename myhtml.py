#!/usr/bin/python
# coding:utf-8
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('1 <%s>' % tag)

    def handle_endtag(self, tag):
        print('2 </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('3 <%s/>' % tag)

    def handle_data(self, data):
        print('4 data')

    def handle_comment(self, data):
        print('5 <!-- -->')

    def handle_entityref(self, name):
        print('6 &%s;' % name)

    def handle_charref(self, name):
        print('7 &#%s;' % name)

parser = MyHTMLParser()
parser.feed(
    '<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END')
