# -*- coding: utf-8 -*-
from selenium import webdriver
profile = webdriver.FirefoxProfile()
# 221.219.100.167:8081
profile.set_preference('network.proxy.type', 1)   #默认值0，就是直接连接；1就是手工配置代理。
profile.set_preference('network.proxy.http', "221.219.100.167")
profile.set_preference('network.proxy.http_port', 8081)
profile.set_preference('network.proxy.ssl', "221.219.100.167")
profile.set_preference('network.proxy.ssl_port', 8081)
profile.update_preferences()
browser = webdriver.Firefox(firefox_profile=profile, executable_path=u"D:\pyCharm\geckodriver.exe")
browser.get("http://www.ip138.com")