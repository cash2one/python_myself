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

import baiduPulldownPc

import json
class FindPicture(object):

    def __init__(self):
        self.baiduPc = baiduPcFunction.PcFunction()
        self.baiduMobile = baiduMobileFunction.MobileFunction()
        self.util = utilsFunction.UtilsFunction()
        self.pcPulldown = baiduPulldownPc.PcFunction()

    def picture_screenshot_html(self, keyword, ckurl, searchDevice, spidertype, searchPage, returnType):
        starttime = datetime.datetime.now()
        picturedata = None
        try:
            if int(searchDevice) == 1:
                browser = webdriver.Firefox(executable_path=sxconfig.geckodriverPath)
                browser.set_page_load_timeout(sxconfig.page_load_timeout)
                browser.set_script_timeout(sxconfig.script_timeout)

                browser.maximize_window()

                # 关闭预测
                # self.closeForeCast(browser)
                browser.get(sxconfig.baiduPcGaoJi)
                options = browser.find_elements_by_tag_name("option")
                # 1,2,3 一页 条数  4,5，6 输入法  7,8 预测
                options[7].click()
                browser.find_element_by_id("save").click()
                time.sleep(1)
                browser.switch_to_alert().accept()
                time.sleep(1)
                self.util.fullloaded(browser)

                browser.find_element_by_id('kw').clear()  # 用于清除输入框的内容
                browser.find_element_by_id('kw').send_keys(u''+keyword)  # 在输入框内输入
                # browser.find_element_by_id('su').click()  # 用于点击按钮
                # browser.find_element_by_id('su').submit()  # 用于提交表单内容

                self.util.fullloaded(browser)

                js = """
                    var products = document.querySelectorAll('.bdsugbg');
                    if(products.length > 0){
                        products[0].style.display = 'block';

                        var overflows = document.querySelectorAll('.bdsug-overflow');
                        for(var i=0; i < overflows.length; i++){
                            if(i == 1){
                                overflows[i].setAttribute('style','box-shadow: 0px 0px 0px 3px #FF0000;');
                                return;
                            }
                        }
                    }
                    """

                browser.execute_script(js)
                print "11"

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

                browser = webdriver.Chrome(executable_path="D:\pyCharm\chromedriver.exe")

                browser.set_page_load_timeout(sxconfig.page_load_timeout)
                browser.set_script_timeout(sxconfig.script_timeout)

                browser.set_window_size(sxconfig.baiduMobileWidth, sxconfig.baiduMobileHeight)
                browser.get(sxconfig.baiduMobileUrl)  # Load page

                browser.find_element_by_id('index-kw').clear()  # 用于清除输入框的内容
                # browser.find_element_by_id('index-kw').click()
                time.sleep(1)
                browser.find_element_by_id('index-kw').send_keys(u'' + keyword)  # 在输入框内输入
                time.sleep(1)

                js = """
                    var box = document.querySelectorAll('#index-box');
                     if(box.length > 0){
                        box[0].style.display = 'block';
                     }
                     var suggest = document.querySelectorAll('.suggest-div');
                     if(suggest.length > 0){
                        suggest[0].style.display = 'block';
                     }

                    var edits = document.querySelectorAll('.sug-edit')
                    var sugs = document.querySelectorAll('.sug');
                    for(var i=0; sugs.length; i++){
                        if(i == 2){
                            sugs[i].setAttribute('style',"border-bottom:3px solid #F00");
                            return;
                        }
                    }
                    """
                # "box-shadow: 0px 3px 0px 3px #FF0000;"
                # edits[i].setAttribute('style', 'box-shadow: 0px 3px 0px 3px #FF0000;');

                # '''
                #   var direct = document.querySelectorAll('.suggest-direct');
                #      if(direct.length > 0){
                #         direct[0].style.display = 'none';
                #         };
                #
                #      var products1 = document.querySelectorAll('.suggest-panel');
                #      if(products1.length > 0){
                #         products1[0].style.display = 'block';
                #         };
                #
                #      var products2 = document.querySelectorAll('.suggest-title');
                #      if(products2.length > 0){
                #         products2[0].style.display = 'block';
                #         };
                #
                #      var products3 = document.querySelectorAll('.suggest-close');
                #      if(products3.length > 0){
                #         products3[0].style.display = 'block';
                #         };
                #
                #      var overflows = document.querySelectorAll('.sug');
                #         for(var i=0; i < overflows.length; i++){
                #
                #             overflows[i].setAttribute('style','box-shadow: 0px 3px 0px 3px #FF0000;');
                #
                #         };
                #
                # '''
                browser.execute_script(js)
                browser.find_element_by_id('index-kw').click()

                # browser.find_element_by_id('index-bn').click()  # 用于点击按钮

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
            return -1
            # browser.quit()

    def closeForeCast(self, browser):
        browser.get(sxconfig.baiduPcGaoJi)
        options = browser.find_elements_by_tag_name("option")
        # 1,2,3 一页 条数  4,5，6 输入法  7,8 预测
        options[7].click()
        browser.find_element_by_id("save").click()
        browser.switch_to_alert().accept()
        # browser.switch_to_default_content()

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
