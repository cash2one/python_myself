# -*- coding: utf-8 -*-
from browsermobproxy import Server
from selenium import webdriver
import json

# ""C:\\browsermob-proxy-2.0-beta-9\\bin\\browsermob-proxy.bat""
server = Server(u"D:/pyCharm\myself_python/browsermob-proxy-2.0-beta-6-bin/browsermob-proxy-2.0-beta-6/bin/browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()

# profile = webdriver.FirefoxProfile()
# profile.set_proxy(proxy.selenium_proxy())
# driver = webdriver.Firefox(firefox_profile=profile)
driver = webdriver.PhantomJS(executable_path=u"E:\python\phantomjs-1.9.7-windows\phantomjs.exe")

proxy.new_har("baidu")
driver.get("http://www.baidu.com")
proxy.wait_for_traffic_to_stop(1, 60)
with open('1.har', 'w') as outfile:
    json.dump(proxy.har, outfile)

server.stop()
driver.quit()