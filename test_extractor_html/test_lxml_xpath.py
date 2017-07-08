# -*- encoding: utf-8 -*-

from lxml.html import fromstring

0
import tld

html_body = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
"""

html_two = """
<html>
<body>
<bookstore position="cn">
    <book category="A">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="B">
        <title lang="en">Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
</bookstore>
<bookstore position="pk">
    <book category="A">
        <title lang="en">Learning XML</title>
        <author>Erik T. Ray</author>
        <year>2003</year>
        <price>39.95</price>
    </book>
</bookstore>
<bookstore position="jp">
    <book category="C">
        <title lang="en">XQuery Kick Start</title>
        <author>James McGovern</author>
        <author>Per Bothner</author>
        <author>Kurt Cagle</author>
        <author>James Linn</author>
        <author>Vaidyanathan Nagarajan</author>
        <year>2003</year>
        <price>49.99</price>
    </book>
</bookstore>
</body>
</html>
"""

html_tree = fromstring(html_body.decode("utf-8", "ignore"))
# book_text =  html_tree.xpath('//bookstore/book')
# print book_text[0].text

li_class = html_tree.xpath("//li/@class")
print li_class
#
# span = html_tree.xpath("//ul//span")
# print span[0].text
#
href_ele = html_tree.xpath('//a[@href="link1.html"]')

# href_ele[0].find("a", string="first item")

# print href_ele[0].xpath('')

# print href_ele[0].xpath('a', {"href": "link1.html"})[0].xpath('string(.)').strip()
# print span[0]
print href_ele[0].text