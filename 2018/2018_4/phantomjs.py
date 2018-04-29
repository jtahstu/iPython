"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/4/24 14:45
"""

from selenium import webdriver

browser = webdriver.Chrome()
driver = webdriver.PhantomJS()
# driver.get("https://www.fyvor.com/")
driver.get("https://www.frcodespromo.com/")
data = driver.get_screenshot_as_file("./ssfr.png")
# print(data)

