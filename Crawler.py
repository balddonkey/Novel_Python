#!/usr/bin/env python3  
 
#%%
from urllib import request, parse
from lxml import etree
import re

i = 1
max_page = 5
while True:
    
    url = 'http://se.qidian.com/?kw='+parse.quote('凡人')+'&page='+str(i)
    f = request.urlopen(url)
    read_data = f.read()
    # content = read_data.decode()
    tree = etree.HTML(read_data, parser=etree.HTMLParser(encoding='utf-8'))
    print('tree:', type(tree))
    nodes = tree.xpath(u"//div[@id='result-list']/div[@class='book-img-text']/ul/li")
    print(len(nodes))
    for n in nodes:
        print('n:', type(n), etree.tostring(n))
        detail = n.xpath(u"div[@class='book-img-box']/a")[0]
        bookname = n.xpath(u"div[@class='book-mid-info']/h4//a")[0].text
        author = n.xpath(u"div[@class='book-mid-info']//p[@class='author']//a[@class='name']")[0].text

        print(detail.attrib['href'], bookname, author)
    i += 1
    if i > max_page:
        break

# tree = etree.HTML(content)
# nodes = tree.xpath(u"//div[@id='result-list']")
# print(nodes[0].text)
# for n in nodes:
#     print(n.text)
    