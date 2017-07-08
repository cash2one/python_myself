# -*- coding: utf8 -*-
from selenium import webdriver

import os
import sys
# PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# sys.path.append(PROJECT_PATH)
# sys.path.append(os.path.join(PROJECT_PATH, 'screenshot'))

import datetime
import time
import sxconfig
import base64
from selenium.common.exceptions import TimeoutException
reload(sys)
sys.setdefaultencoding('utf-8')

import baiduPcFunction
import baiduMobileFunction
import utilsFunction

import json
class FindPicture(object):

    def __init__(self):
        self.baiduPc = baiduPcFunction.PcFunction()
        self.baiduMobile = baiduMobileFunction.MobileFunction()
        self.util = utilsFunction.UtilsFunction()

    def picture_screenshot_html(self, keyword, ckurl, searchDevice, spidertype, searchPage, returnType):
        starttime = datetime.datetime.now()
        picturedata = None
        try:
            if int(searchDevice) == 1:
                browser = webdriver.Firefox(executable_path=sxconfig.geckodriverPath)
                browser.set_page_load_timeout(sxconfig.page_load_timeout)
                browser.set_script_timeout(sxconfig.script_timeout)

                browser.maximize_window()
                browser.get(sxconfig.baiduPcUrl)  # Load page
                browser.find_element_by_id('kw').clear()  # 用于清除输入框的内容
                browser.find_element_by_id('kw').send_keys(u''+keyword)  # 在输入框内输入
                browser.find_element_by_id('su').click()  # 用于点击按钮
                browser.find_element_by_id('su').submit()  # 用于提交表单内容

                # browser.find_element_by_name("")

                self.util.fullloaded(browser)

                for currentpage in xrange(1, searchPage+1):
                    # print currentpage
                    # print browser.current_url
                    jsClientWidth = '''return document.body.clientWidth'''
                    tatalWidth = browser.execute_script(jsClientWidth)
                    # print tatalWidth
                    jsScrollHeight = '''return  document.body.parentNode.scrollHeight'''
                    tatalHeight = browser.execute_script(jsScrollHeight)
                    # print tatalHeight

                    html_source = browser.page_source  # 页面
                    if int(returnType) > 0:
                        # 根据页面返回排名 数组
                        rankitem = self.baiduPc.getRankListByHtmlPc(html_source, ckurl, spidertype)

                        ranklist = rankitem['rankList']
                        nextPageUrl = rankitem['nextPageUrl']

                        if len(ranklist) > 0:
                            picturedata = self.baiduPc.getPictureAndScreenPc(browser, ranklist, tatalWidth, tatalHeight, returnType)
                            break
                        else:
                            if currentpage == 5:
                                break
                            if nextPageUrl is None:
                                break
                            browser.get(sxconfig.baiduPcUrl+nextPageUrl)
                            self.util.fullloaded(browser)
                    else:
                        break
            else:
                # mobile
                firefoxProfile = webdriver.FirefoxProfile()
                # 设置 useragent
                firefoxProfile.set_preference("general.useragent.override",
                                              sxconfig.mobileUserAgent)
                browser = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=sxconfig.geckodriverPath)

                browser.set_page_load_timeout(sxconfig.page_load_timeout)
                browser.set_script_timeout(sxconfig.script_timeout)

                browser.set_window_size(sxconfig.baiduMobileWidth, sxconfig.baiduMobileHeight)
                browser.get(sxconfig.baiduMobileUrl)  # Load page
                browser.find_element_by_id('index-kw').clear()  # 用于清除输入框的内容
                browser.find_element_by_id('index-kw').send_keys(u'' + keyword)  # 在输入框内输入
                browser.find_element_by_id('index-bn').click()  # 用于点击按钮

                self.util.fullloaded(browser)
                for currentpage in xrange(1, searchPage + 1):
                    html_source = browser.page_source  # 页面
                    if int(returnType) > 0:
                        # 根据页面返回排名 数组
                        rankitem = self.baiduMobile.getRankListByHtmlMobile(html_source, ckurl, spidertype)
                        ranklist = rankitem['rankList']
                        nextPageUrl = rankitem['nextPageUrl']
                        if len(ranklist) > 0:
                            picturedata = self.baiduMobile.getPictureAndScreenMobile(browser, ranklist,
                                               sxconfig.baiduMobileWidth, sxconfig.baiduMobileHeight, returnType)
                            break
                        else:
                            if currentpage == 5:
                                break
                            if nextPageUrl is None:
                                break
                            browser.get(nextPageUrl)
                            self.util.fullloaded(browser)
                    else:
                        break
            browser.delete_all_cookies()
            browser.close()
            # browser.quit()

            endtime = datetime.datetime.now()
            print ((endtime - starttime).seconds)
            if picturedata:
                picturedata["html"] = html_source
                picturedata["page"] = currentpage
                return json.dumps(picturedata)
            else:
                return -2
        except Exception, e:
            print e
            browser.close()
            # browser.quit()

if __name__ == "__main__":
    sx = FindPicture()
    # url = '''https://www.baidu.com'''
    # keyword, ckurl, searchDevice, spidertype, searchPage, returnType
    # data = sx.picture_screenshot_html("租房", ".51job.com", 2, 1, 5 ,"1100")

    data = sx.picture_screenshot_html("招聘", ".51job.com", 2, 1, 5, "1111")
    # data = sx.picture_screenshot_html("招聘", "www.job5156.com", 2, 1, 5, "1111")
    # data = sx.picture_screenshot_html("招聘", "www.hrm.cn", 2, 1, 5, "1111")

    # data = sx.picture_screenshot_html("招聘", "m.yingjiesheng.com", 2, 1, 5, "0010")
    # data = sx.picture_screenshot_html("贝因美", ".qqbaobao.com", 2, 1, 5, "1010")

    # data = sx.picture_screenshot_html("招聘", ".zhaopin.com", 1, 1, 5, "1100")
    # data = sx.picture_screenshot_html("招聘", ".qlrc.com", 1, 1, 5, "1111")

    if data is not None:
        sx_dataDict = json.loads(data)
        i = 1
        if "capture" in sx_dataDict:
            sxcapture = base64.b64decode(sx_dataDict["capture"])
            file = open("%scapture.png" % i, "wb")
            file.write(sxcapture)
            file.close()
        if "capture_red" in sx_dataDict:
            sxcapture = base64.b64decode(sx_dataDict["capture_red"])
            file = open("%scapture_red.png" % i, "wb")
            file.write(sxcapture)
            file.close()
        if "screenshot" in sx_dataDict:
            sxcapture = base64.b64decode(sx_dataDict["screenshot"])
            file = open("%sscreenshot.png" % i, "wb")
            file.write(sxcapture)
            file.close()
        if "screenshot_red" in sx_dataDict:
            sxcapture = base64.b64decode(sx_dataDict["screenshot_red"])
            file = open("%sscreenshot_red.png" % i, "wb")
            file.write(sxcapture)
            file.close()
    else:
        print "no rank "
    # 调用 windows 命令行
    import os
    command = "taskkill /f /im firefox.exe /t"  # 在command = "这里填写要输入的命令"
    os.system(command)
    # command = "taskkill /f /im WerFault.exe /t"  # 在command = "这里填写要输入的命令"
    # os.system(command)
