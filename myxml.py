#!/usr/bin/python
# coding:utf-8
from xml.parsers.expat import ParserCreate


class MySaxHandler(object):

    def start(self, name, attrs):
        print('sax:start_element:%s ,attrs:%s' % (name, str(attrs)))

    def end(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = MySaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start
parser.EndElementHandler = handler.end
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


def encode(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some & data'))
L.append(r'</root>')
print ''.join(L)
