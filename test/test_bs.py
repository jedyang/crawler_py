# coding:utf8

import re

from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding = 'utf8')
print '获取所有链接'
links = soup.findAll('a')
for link in links:
    print link.name,link['href'],link.get_text()

print '获取指定链接'
## href的内容必须写全
link = soup.find('a', href = 'http://example.com/lacie')
print link.name,link['href'],link.get_text()


print '正则匹配'
link = soup.find('a', href = re.compile(r'lacie'))
print link.name,link['href'],link.get_text()

print '获取段落'

p = soup.find('p',class_='title')
print p.name,p.get_text()

