#!/usr/bin/python
# coding=utf-8

import lxml.etree

doc = lxml.etree.parse("test.xml")

root = doc.getroot()#获得该树的树根

for article in root:#这样便可以遍历根元素的所有子元素(这里是article元素)
     print "元素名称：",article.tag#用.tag得到该子元素的名称
     for field in article:#遍历article元素的所有子元素(这里是指article的author，title，volume，year等)
         print field.tag,":",field.text#同样地，用.tag可以得到元素的名称，而.text可以得到元素的内容
     mdate=article.get("mdate")#用.get("属性名")可以得到article元素相应属性的值
     key=article.get("key")
     print "mdate:",mdate
     print "key",key
     print ""#隔行分开不同的article元素


# for node in doc.xpath("//country/neighbor[@name = $name]", name="Colombia"):

# for node in doc.xpath("//country/neighbor[@name = 'Colombia']"):
#     print node.tag, node.items()
#     print "几点几分的"
# for node in doc.xpath("//country[@name = $name]", name="Singapore"):
#     print node.tag, node.items()