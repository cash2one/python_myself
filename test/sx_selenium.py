
# -*- coding: UTF-8 -*-

import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.set_window_size(1055, 800)
browser.get("http://www.yooli.com/")
browser.find_element_by_id("idClose").click()
time.sleep(5)

browser.save_screenshot("shot2.png")
browser.quit()