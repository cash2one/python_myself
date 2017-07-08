#coding:utf-8
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
# driver = webdriver.Chrome(r"E:\python\jietu\chromedriver_win32\chromedriver.exe")

# , chrome_options=options
# u"E:\python\jietu\chromedriver_win32\chromedriver.exe",
driver = webdriver.Chrome( chrome_options=options)

# driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Update\chromedriver.exe")
driver.get("https://www.baidu.com/?tn=78040160_5_pg&ch=1")
driver.find_element_by_id("kw").send_keys(u"智普教育")
driver.find_element_by_id("su").click()