# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import sxconfig
import json
import time

import utilsFunction
import domain_urllib

class MobileFunction(object):

    def __init__(self):
        self.util = utilsFunction.UtilsFunction()
        self.domainUtil = domain_urllib.SeoDomain()

    def getRankListByHtmlMobile(self, body, ck, spidertype):
        rankitem = {}
        rankList = list()
        pos = body.find("</html>")
        nextPageUrl = None

        if pos < 0:
            pass
        else:
            try:
                bsObj = BeautifulSoup(body, "lxml")

                nextPageUrlList = bsObj.find_all("a", {"class": "new-nextpage-only"})
                if nextPageUrlList:
                    nextPageUrl = nextPageUrlList[0].attrs['href']
                    # print nextPageUrl
                else:
                    nextPageUrlList = bsObj.find_all("a", {"class": "new-nextpage"})
                    if nextPageUrlList:
                        nextPageUrl = nextPageUrlList[0].attrs['href']
                        # print nextPageUrl
                containers = bsObj.find_all("div", {"class": "c-result"})

                if len(containers) > 0:
                    for container in containers:
                        toprank = ""
                        title = ''
                        des = ''  # 描述
                        evaluate = ""  # 评价
                        realaddress = ""
                        domain = ""

                        order = int(container.attrs['order'])
                        if order:
                            toprank = order

                        domain_list = container.find_all("a", {"class": "c-showurl"})
                        if len(domain_list) > 0:
                            domain = domain_list[0].get_text().strip()
                        else:
                            domain_list = container.find_all("span", {"class": "c-showurl"})
                            if len(domain_list) > 0:
                                domain = domain_list[0].get_text().strip()
                        if ck:
                            # 根据domain  和 给出的url 匹配

                            datalog = container.attrs['data-log']
                            if datalog:
                                datalog = str(datalog).replace("\'", "\"")
                                sx_data = json.loads(datalog)
                                mu_url = sx_data["mu"]
                                if int(spidertype) == 2:
                                    # 提供url 和 真实url 相等
                                    if mu_url == ck:
                                        pass
                                    else:
                                        continue
                                else:
                                    mu_urlDomain = self.domainUtil.sxGetDomain(mu_url)
                                    ck_domain = self.domainUtil.sxGetDomain(ck)
                                    if mu_urlDomain != "" and ck_domain != "":
                                        if mu_urlDomain == ck_domain:
                                            pass
                                        else:
                                            continue
                                    else:
                                        continue
                            else:
                                continue
                        rankList.append(str(toprank))
                else:
                    pass
            except Exception, e:
                print "mobileFunction"
                print e
        rankitem['rankList'] = rankList
        rankitem['nextPageUrl'] = nextPageUrl
        return rankitem

    def getPictureAndScreenMobile(self, browser, ranklist, tatalWidth, tatalHeight, returnType):
        returnDataDict = {}

        self.util.fullloaded(browser)
        tatalHeightjs = '''return  document.body.scrollHeight'''
        tatalHeight = browser.execute_script(tatalHeightjs)
        # print tatalHeight
        mobileHeight = tatalHeight + sxconfig.mobileAddHeight
        mobileRedHeight = tatalHeight + (sxconfig.borderWidth * len(ranklist) * 2) + sxconfig.mobileAddHeight


        if int(returnType[0:1]) == 1:
            browser.set_window_size(tatalWidth, mobileHeight)
            capture = browser.get_screenshot_as_base64()  # 图片
            returnDataDict["capture"] = capture

        if int(returnType[1:2]) == 1:
            browser.set_window_size(sxconfig.baiduMobileWidth, sxconfig.baiduMobileHeight)
            if len(ranklist) > 0:
                rank = int(ranklist[0])
                if rank > 2:
                    jselement = """
                                var products = document.querySelectorAll('.c-result');
                                for(var i=0;i<products.length;i++){
                                    if(products[i].getAttribute('order')=='%d'){
                                        return products[i];
                                    }
                                }
                                """ % (int(rank)-1)
                    # sxelement = browser.find_element_by_id("" + str(rank - 1))
                    sxelement = browser.execute_script(jselement)
                    browser.execute_script("arguments[0].scrollIntoView();", sxelement)
            screenshot = browser.get_screenshot_as_base64()  # 图片
            if screenshot:
                returnDataDict["screenshot"] = screenshot
            else:
                return None

        for rank in ranklist:
            js = "var products = document.querySelectorAll('.c-result');" \
                     " for(var i=0;i<products.length;i++){	if(products[i].getAttribute('order')=='%d'){	" \
                     " containers = products[i].querySelectorAll('.c-container');" \
                     "containers[0].setAttribute('style','border: %dpx solid red;');" \
                     "return;}};"  % (int(rank), sxconfig.borderWidth)
                     # "var div = document.createElement('div');" \
                     # " div.setAttribute('style', 'width:100px;height:20px;');" \
                     # "document.body.appendChild(div);" % (int(rank), sxconfig.borderWidth)
            # (int(rank), sxconfig.borderWidth)
            browser.execute_script(js)
        if int(returnType[2:3]) == 1:
            browser.set_window_size(tatalWidth, mobileRedHeight)
            capture_red = browser.get_screenshot_as_base64()  # 图片
            returnDataDict["capture_red"] = capture_red

        if int(returnType[3:4]) == 1:
            browser.set_window_size(sxconfig.baiduMobileWidth, sxconfig.baiduMobileHeight)
            if len(ranklist) > 0:
                rank = int(ranklist[0])
                if rank > 2:
                    jselement = """
                                var products = document.querySelectorAll('.c-result');
                                for(var i=0;i<products.length;i++){
                                    if(products[i].getAttribute('order')=='%d'){
                                        return products[i];
                                    }
                                }
                                """ % (int(rank)-1)
                    # sxelement = browser.find_element_by_id("" + str(rank - 1))
                    sxelement = browser.execute_script(jselement)
                    browser.execute_script("arguments[0].scrollIntoView();", sxelement)
            screenshot_red = browser.get_screenshot_as_base64()  # 图片
            if screenshot_red:
                returnDataDict["screenshot_red"] = screenshot_red
            else:
                return None
        return returnDataDict
