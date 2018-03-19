#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#%%
import re

p = re.compile('\[\s+1\]')  

ss = '0x100004688	0x00000220	[  1] -[ViewController viewDidLoad]'

result = p.findall(ss)
print(result)

#%%
import re

emre = re.compile('^\w+@\w+[.]\w{2,}$|^(\+?86[-|\s]?)?1[\d]{10}$')

sss = 'michaellearnsrock@163.com' # '+8618516601886'

emres = emre.match(sss)
if emres:
    print(emres)
    print(emres.group())
    print(emres.start(), emres.end())
    print(emres.span())
else: 
    print(emres)

#%%
import re

# 分组
p2 = re.compile('(a(b)(c)d)e')

m2 = p2.match('abcde')
print(m2.groups())
m2_fa = p2.findall('abcde')
print('m2_fa:', m2_fa)

m3 = re.match('(a(b)c)d', 'abcd')
print(m3.groups())

#%% 丢雷老谋
import re

p = re.compile(r'\b(\w+)\s+\1{1,}')
r = p.search('the thetheParis in spring')
print(r.span())
# print(m.group())
for g in r.group():
    print(g)

str2 = 'aba  aba aba aba bcsad'
p2 = re.compile(r'(\b\w+\s+)\1{2,}')
search2 = p2.search(str2)
if search2:
    print(search2.group())
    for g2 in search2.group():
        print(g2)
else:
    print(search2)
group2 = p2.findall(str2)
print(group2)

#%% 字符串分割
import re

comStr = 'This... is a test.'
p = re.compile(r'\W+')
print(p.split(comStr))

p2 = re.compile(r'(\W+)')
print(p2.split(comStr))

#%% 字符串搜索&替换
import re

p1 = re.compile('(blue|white|red)')
str1 = 'blue socks and red shoes'
sub1 = p1.sub('colour', str1)
print(sub1)
sub1 = p1.sub('colour', str1, count=1)
print(sub1)

p2 = re.compile('x*')
print(p2.sub('-', 'abxd'))

#%% 字符串搜索&替换 -- 2
import re

str1 = 'section{{first}} section{second}}'
p1 = re.compile('section{+ (?P<num> [^{|^}]* ) }+', re.VERBOSE)
search = p1.search(str1)
print(search.groups())

print(p1.sub(r'subsection{\1}', str1))
print(p1.sub(r'subsection{\g<1>}', str1))
print(p1.sub(r'subsection{\g<num>}', str1))


#%% 字符串搜索&替换 -- 函数

def hexrepl( match ):
    value = int( match.group() )
    return hex(value)

p = re.compile(r'(\d+)+')
# result = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
# print(result)
s = p.finditer('Call 65490 for printing, 49152 for user code.')
for iter in s:
    print('zz')
    print(iter.group())


# re.subn ...


#%% 前向界定符
p = re.compile(r'.*[.](?!bat$).*$')
s = 'hehe.battlenet'
print(p.match(s).group())

p = re.compile(r'.*[.](?=bar)')
s = 'hehe.barrent'
print(p.match(s).group())

#%% parse html
import re

# r'<(\w+)(?!>\s+.{0,})?>(.*)</\1>'
# <(\w+)(?!>\s+.*?)?(\s*?a)(?!>\s+.*?)?>(.*)</\1>

str1 = '<html a="bb">111<body><a>hehehe</a></body></html>'
strres = re.sub('\s', '', str1)
p = re.compile(r'<(\w+)(?!>.*?)?(\s*?a="bb")(?!>.*?)?>(.*)</\1>', re.DOTALL)
result = p.search(str1)
print(result.group(3))

# print('2', result.group(2))
# print('3', result.group(3))
# result = p.search(result.group(3))
# print(result.group(3))
# result = p.search(result.group(3))
# print(result.group(3))
