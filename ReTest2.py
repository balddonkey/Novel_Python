
#%% 
import re

test = "aaa bbbb ffffff 999999999";
p = re.compile(r"(\w)((?=\1\1\1)(\1))+")

mat = p.finditer(test)
for gen in mat:
    print(gen.group())
    print(gen.span())
    print(gen.start(), gen.end())

#%%

import re

s2 = 'ab0cdebb0cde'
p2 = re.compile(r'(?P<hehe>[ab])(?P=hehe)')
f = p.finditer(s2)
for iter in f:
    print(iter.group())

#%%
import re

s3 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz aasdaasd'
p3 = re.compile(r'(?P<hehe>[a-z]+)(?P=hehe)+')
f3 = p3.finditer(s3)
print(p3.findall(s3))
for iter3 in f3:
    print('hehe')
    print(iter3.group(), ' ')
    print(iter3.groups())


#%%
import re
s4 = '''南荒，玄国，玄女派杨师妹等五女每个人心情可谓极好，将这一日将要出售物品在两个时辰内就被抢购一空后，她们就关闭了混杂铺，在别人羡慕的眼神下，携带着大量的灵石向北悦后山而去。

    她们来到这巨灵城将近一年了，本来在刚入巨灵城的那一段时间，人人经过最初的兴奋后，她们很快心情极为糟糕，在这繁华的巨灵城很难生存下去，巨灵城的巨大消耗令她们迫于无奈都想着出卖自己了。

    结果在她们忧愁无助时，闵瑄师叔突然宣布她们这些玄国来的孤魂野鬼被一位元婴期的混玄老祖看中，支持组建一个名为混玄宗的宗门。

    这令杨师妹等人心中失落之极，感觉自己最终还是被出售了么？

    只是她们被出售给了一位元婴老祖吧？

    不过当初的大师姐，此刻的闵瑄师叔很快打消了他们的顾虑，明言这混玄老祖是一位出自南荒元婴老祖，对于来自南荒的她们这些孤魂野鬼十分同情，决定帮一把，并不会有丝毫的所求。

    路遥知马力日久见人心，虽然一直没要见过那位混玄老祖，但她们的处境无疑一步步提升起来，

    在北悦客栈待了一个月后，杨师妹她们就匪夷所思地搬入了北悦后山的一座方圆十余里的山峰，在这寸土寸金的巨灵城，据说这座山峰仅仅一年的租赁费用就是一亿多下品灵石，这令她们猛然欣喜若狂起来。

    然而令她们欣喜的远远不止这些，因为那位混玄老祖简直不知富裕到何种程度，除了租赁下北悦后山的灵气极为浓郁的洞府外，竟然还出资海量灵石培养他们，无论是你想从事炼制丹药、符篆、法器、阵法等修仙百艺，哪一样都行，只要你有浓厚兴趣就行。

    如果对于这些修真百艺都不感兴趣只想专心修炼也行，混玄宗也会提供海量资源供你修行，只要提出自己的修炼规划，向混玄宗执事长老提出申请就行，一般都会得到批准，只是时间长短不同罢了。

    并且混玄老祖承诺尽混玄宗最大的努力，保证第一批加入混玄宗的修士给每人提供一次结丹的机会，而这种结丹机会通常是混玄宗提供两到三种辅助凝结金丹的圣药。

    当然这种天上掉馅饼的好处也不是完全没有条件的，那就是必须绝对服从混玄老祖命令，毕竟培养他们每一人花费的资源都非常庞大，长久下来，即使混玄老祖估计也会吃不消的，若是白白培养他们也不现实。

    事实上只有这个条件才打消了很多人的顾虑，否则这一切简直太多匪夷所思了。

    于是所有人略微一思索后就加入了，有些还有顾虑的修士则在原宗门金丹师叔的。

    毕竟第一凝结金丹的诱惑实在太大，他们九死一生也不见得能够弄到一两种辅助凝结金丹的圣药。

    第二混玄老祖提出的条件虽然苛刻，要求他们必须绝对服从他的命令，甚至都将一缕本命精魂交了出去，但混玄老祖承诺绝不会刻意刁难，比如强要美色之类，也不会无故令他们充当炮灰，并且只需在混玄宗一直培养这他们的一百年内听命混玄老祖，一百年后去留自由。

    【ps：因此书成绩差，所以就切了，若是现在长回来，还有人支持么？】'''
p4 = re.compile(r'([\S]+)')
f4 = p4.finditer(s4)
print(p4.findall(s4))
if f4:
    for iter4 in f4:
        print('aaa')
        print(iter4.span())
else:
    print('bbb')
    print(f4)


#%%
from urllib import request, parse
from lxml import etree
import re
import unicodedata
import string

url = "http://www.biqudu.com/0_401/1449571.html"
f = request.urlopen(url)
read_data = f.read()

xp = '//div[@id="content"]'
tree = etree.HTML(read_data, parser=etree.HTMLParser(encoding='utf-8'))
node = tree.xpath(xp)[0]
print(etree.tostring(node, method='text', encoding='utf-8'))
text_content = etree.tostring(node)
content = str(text_content, encoding='utf-8')

print(type(content))
print(content)
# print(text_content)
brre = re.compile(r'(<br/>)')
content = brre.sub('', content)
print(content)

tr = etree.HTML(content)
print(etree.tostring(tr, method='text', encoding='unicode'))
# content = str(text_content)
# content = unicodedata.normalize("NFKD", content)
# print(type(content))
# re = re.compile(r'([\s]+)', re.MULTILINE)
# print(re.findall(content))
# rr = re.finditer(content)
# for interr in rr:
#     print('heihei')
#     print(interr.group(), interr.span())
#     print('haha')



#%%
import re

st5 = '''[self p1:@"hehe" p2:@"haha" p3:@"heihei"]'''
p5 = re.compile(r'\[.+?(?P<aa>\s+(\S+:\S+)\s*)+?\]')
s5 = p5.finditer(st5)
print(p5.findall(st5))
for iter in s5:
    print('heihei')
    print(iter.span('aa'))
    print(iter.group('aa'))

pp = re.compile(r'\[\S+?\s(\S+)\]')
print(pp.findall(st5))

print(hex(65535))
