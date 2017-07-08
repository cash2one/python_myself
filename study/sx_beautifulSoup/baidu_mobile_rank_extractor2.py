#coding=utf8
import os
import sys
import re
# from bs4 import BeautifulSoup
import datetime
import time
# reload(sys)
sys.setdefaultencoding('utf8')
class BaiduMobileRankExtractor (object):

    def __init__(self):
        super(BaiduMobileRankExtractor, self).__init__()        

    '''
          获取移动排名数据
    '''
    def extractor(self, body, ck='', cktitle=''):
	time_a = time.time()
        li = list()
        ranks = {}
        li.append(ranks)
        pos = body.find("</html>")
        if body.find('id="page-bd"') < 0 or pos < 0:
            # 页面不全
            ranks['response_status'] = 2
            return li
        if body.find('抱歉，没有找到与') > 0:
            ranks['response_status'] = 0
            return li
	ranks['response_status'] = 1
        ranks['rank'] = []
        dr = re.compile(r'<[^>]+>', re.S)
        body = re.sub('\s', '', body)
        reshtml = re.findall(r'(<divid="results"class="results">.*?<\/div>)<divid="page-relative">', body)
        if not reshtml:
            ranks['response_status'] = 0
            return li
        body = reshtml[0]
        #if re.search('<divclass="reswrap">',body):
        #    divlist = re.findall(r'<divclass="resitem".*?>(.*)<\/div><\/div>',body) 
        #    print len(divlist)
        #return li
        #divlist = re.findall(r'(<divid="results"class="results">.*?<\/div>)<divid="page-relative">',body)
        xlist = re.findall(r'(<div.*?order="\d+".*?>.*?</div></div>)', body)
        toprank = 1
        if not xlist:
            ranks['response_status'] = 0
            return li
        for x in xlist:
            title = ''
            des = ''
            domain = ''
            pos = 0
            srcid = ''
            rank = toprank
            if re.search('tpl="www_normal"', x):
                domain_list = re.findall(r"'mu':'(.*?)'", x)
                if domain_list:
                    domain = domain_list[0]
            if re.search('<spanclass="c-showurl">', x):
                domain_list = re.findall(r'<spanclass="c-showurl">(.*?)<\/span>', x)
            else:
                domain_list = re.findall(r'<a.*?class="c-showurl".*?>(.*?)<\/a>', x)
            if domain_list:
                domain = dr.sub('', domain_list[0])
            if ck:
                if not re.search(ck, domain):
                    toprank += 1
                    continue
            if re.search('class="result-op', x):
                pos = 4
            if re.search('<aclass="c-blockac-titlec-gap-top-smallc-line-clamp2"', x):
                title_list = re.findall(r'<aclass="c-blockac-titlec-gap-top-smallc-line-clamp2".*?>(.*?)<\/a>', x)
            else:
                title_list = re.findall(r'<h3.*?>(.*?)<\/h3>', x)
            if title_list:
                title = dr.sub('', title_list[0])
                title = re.sub(r'\s', '', title)
            if cktitle:
                if not re.search(cktitle, title):
                    toprank += 1
                    continue
            if re.search('class="wz-generalmaphotel-mapc-gap-top"', x):
                des = 'map'
                domain = 'map.baidu.com'
            elif re.search(u'百度百科', title):
                des = 'baike.baidu.com'
                domain = 'baike.baidu.com'
            else:
                deslist = re.findall(r'<p.*?>(.*?)<\/p>',x)
                if deslist:
                    des = dr.sub('', deslist[0])
            if domain == '' and re.search(u'百度手机助手',title) > 0:
                domain = 'mobile.baidu.com'
            if domain == '' and re.search(u'_相关信息',title) > 0:
                domain = 'm.baidu.com'
            if domain == '' and re.search(u'_相关网站',title) > 0:
                domain = 'm.baidu.com'
            if domain == '' and re.search(u'_百度糯米',title) > 0:
                domain = 'nuomi.baidu.com'
            srcids =  re.findall(r'srcid="(\w+?)"',x)
            if srcids:  
                srcid = srcids[0]
            toprank+=1
            item = {}
            item['domain'] = domain
            item['srcid'] = srcid
            item['pos'] = pos
            item['rank'] = rank
            item['title'] = title
            item['description'] = des
            ranks['rank'].append(item)
            if ck:
                return li
        return li 

if __name__ == '__main__':
    f = open('baidu.html','r')
    content = f.read()
    f.close()
    import time
    for i in range(1):
	a = time.time()
        b = BaiduMobileRankExtractor()
        l_s = b.extractor(content,'51job')
        print l_s
        ranks = l_s[0]['rank']
        print time.time() - a
        for rank in ranks:
	    for r in rank:
	        #continue
	        print r,rank[r]
	    print '\n'
