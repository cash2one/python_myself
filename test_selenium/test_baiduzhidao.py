# -*- coding: utf-8 -*-

from selenium import webdriver
browser = webdriver.Firefox(executable_path=u"D:\pyCharm\geckodriver.exe")
# browser = webdriver.PhantomJS(executable_path=sxconfig.phantomJs)
# browser.set_page_load_timeout(20)
# browser.set_script_timeout(20)

browser.maximize_window()
browser.get("https://zhidao.baidu.com/question/101061832.html")  # Load page

browser.find_element_by_id('60-num').click()  # 用于点击按钮

print "11"