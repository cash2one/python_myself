# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import sxconfig
import json

import domain_urllib
import utilsFunction

class PcFunction(object):

    def __init__(self):
        self.util = utilsFunction.UtilsFunction()
        self.domainUtil = domain_urllib.SeoDomain()

    def getRankListByHtmlPc(self, body, ck, spidertype):
        rankitem = {}
        rankList = list()
        nextPageUrl = None

        pos = body.find("</html>")
        if pos < 0 or body.find('location.href.replace') >= 0:
            pass
        elif body.find('id="wrap"') >= 0 or body.find('<title>') < 0 or body.find('页面不存在_百度搜索') >= 0 \
                or body.find('id="container"') < 0 or body.find('id="content_left"') < 0:
            pass
        else:
            try:
                bsObj = BeautifulSoup(body, "lxml")

                nextPagelist = bsObj.find_all("a", {"class": "n"})

                if len(nextPagelist) > 0:
                    nextPageCount = len(nextPagelist) - 1
                    nextPageUrl = nextPagelist[nextPageCount].attrs["href"]

                containers = bsObj.find_all("div", {"class": "c-container"})
                if len(containers) > 0:
                    for container in containers:
                        toprank = ""
                        title = ''
                        des = ''  # 描述
                        evaluate = ""  # 评价
                        realaddress = ""
                        domain = ""
                        toprank = container.attrs["id"]

                        realaddress_list = container.find_all("a")
                        if len(realaddress_list) > 0:
                            realaddress = realaddress_list[0].attrs["href"]

                        domain_list = container.find_all("a", {"class": "c-showurl"})
                        if len(domain_list) > 0:
                            domain = domain_list[0].get_text().strip()
                        else:
                            domain_list = container.find_all("span", {"class": "c-showurl"})
                            if len(domain_list) > 0:
                                domain = domain_list[0].get_text().strip()
                        if ck:
                            # 根据domain  和 给出的url 匹配
                            # domain 为空 跳过
                            # 提供的 url domain > 10 是 显示url 的domain 以 提供url 的domain 开头
                            # 提供的 url domain < 10  完全相等
                            # domain 解析为空 可能是 百度产品
                            if domain == "":
                                continue
                            # [0:15]
                            # 文件提供的url
                            ck_domain = self.domainUtil.sxGetDomain(ck)
                            show_domain = self.domainUtil.sxGetDomain(domain)[0:10]

                            if show_domain == "":
                                continue
                            if ck_domain.find(show_domain) > -1:
                                realaddress = self.util.findReal_Address(realaddress)  # 真实url
                                if int(spidertype) == 2:
                                    # 提供url 和 真实url 相等
                                    if ck == realaddress:
                                        pass
                                    else:
                                        continue
                                else:
                                    realaddress_domain = self.domainUtil.sxGetDomain(realaddress)

                                    if ck_domain != "" and realaddress_domain != "":
                                        if ck_domain == realaddress_domain:
                                            pass
                                        else:
                                            continue
                                    else:
                                        # print "ck_domain  or show_domain  have  kong ck:" + ck_domain + ",show:" + realaddress_domain
                                        continue
                            else:
                                continue
                        rankList.append(toprank)
                else:
                    pass
            except Exception, e:
                print e
        rankitem['rankList'] = rankList
        rankitem['nextPageUrl'] = nextPageUrl
        return rankitem

    def getPictureAndScreenPc(self, browser, ranklist, tatalWidth, tatalHeight, returnType):
        returnDataDict = {}
        pcHeight = tatalHeight + sxconfig.pcHeightAdd
        pcRedHeight = tatalHeight + (sxconfig.borderWidth * len(ranklist) * 2) + sxconfig.pcHeightAdd
        browser.set_window_size(tatalWidth, pcHeight)  # 改变窗口
        if int(returnType[0:1]) == 1:
            capture = browser.get_screenshot_as_base64()  # 图片
            returnDataDict["capture"] = capture

        if int(returnType[1:2]) == 1:
            browser.maximize_window()
            if len(ranklist) > 0:
                rank = int(ranklist[0])
                if rank > 2:
                    sxelement = browser.find_element_by_id("" + str(rank - 1))
                    browser.execute_script("arguments[0].scrollIntoView();", sxelement)

            screenshot = self.util.getScreenshot(sxconfig.fileNamePicture) # 截屏
            if screenshot:
                returnDataDict["screenshot"] = screenshot
            else:
                return None

        for rank in ranklist:
            js = "var products = document.querySelectorAll('.c-container');" \
                 " for(var i=0;i<products.length;i++){	if(products[i].getAttribute('id')=='%d'){	" \
                 "products[i].setAttribute('style','box-shadow: 0px 3px 0px 10px #FF0000;');return i+'';}}" % int(rank)
            browser.execute_script(js)

        if int(returnType[2:3]) == 1:
            browser.set_window_size(tatalWidth, pcRedHeight)
            capture_red = browser.get_screenshot_as_base64()  # 图片
            returnDataDict["capture_red"] = capture_red

        if int(returnType[3:4]) == 1:
            browser.maximize_window()
            if len(ranklist) > 0:
                rank = int(ranklist[0])
                if rank > 2:
                    sxelement = browser.find_element_by_id("" + str(rank - 1))
                    browser.execute_script("arguments[0].scrollIntoView();", sxelement)
            screenshot_red = self.util.getScreenshot(sxconfig.fileNamePicture)
            if screenshot_red:
                returnDataDict["screenshot_red"] = screenshot_red
            else:
                return None
        return returnDataDict

    def closeForeCast(self, browser):
        browser.get(sxconfig.baiduPcGaoJi)
        options = browser.find_elements_by_tag_name("option")
        # 1,2,3 一页 条数  4,5，6 输入法  7,8 预测
        options[7].click()
        browser.find_element_by_id("save").click()
        browser.switch_to_alert().accept()
        browser.switch_to_default_content()
