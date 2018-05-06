"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/4/24 14:55
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://www.taobao.com")
input_first = browser.find_element(By.ID, "q")
print(input_first)
browser.close()
