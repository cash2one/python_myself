# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
import pickle

# geckodriverPath = u"D:\pyCharm\geckodriver.exe"
# browser = webdriver.Firefox(executable_path=sxconfig.geckodriverPath)

phantomJs = u"E:\python\phantomjs-1.9.7-windows\phantomjs.exe"
driver=webdriver.PhantomJS(executable_path=phantomJs)

username = "yirhpx@163.com"
password = "a30464"

driver.get('http://index.baidu.com/?tpl=trend&word=%D0%DB%B0%B2%D0%C2%C7%F8')
e1 = driver.find_element_by_id("TANGRAM_12__userName")
e1.send_keys(username)
e2 = driver.find_element_by_id("TANGRAM_12__password")
e2.send_keys(password)
e3 = driver.find_element_by_id("TANGRAM_12__submit")
e3.click()
cookies = driver.get_cookies()

print cookies
time.sleep(6)

pickle.dump(cookies, open("cookies.txt","wb"))

with open("cook.txt", "wb") as f:
    f.write(str(cookies))