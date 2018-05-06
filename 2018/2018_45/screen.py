"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/4/24 14:45
"""

# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# # driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Firefox()
# # driver.get("https://www.fyvor.com/")
# driver.get("https://www.baidu.com/")
# data = driver.get_screenshot_as_file("./baidu.png")
# # print(data)
# driver.close()


# from selenium import webdriver
# options=webdriver.ChromeOptions()
# options.set_headless()
# # options.add_argument(‘--headless‘)
# options.add_argument('--disable-gpu')
# driver=webdriver.Chrome(options=options)
# driver.get('http://httpbin.org/user-agent')
# driver.get_screenshot_as_file('test.png')
# driver.close()


# from selenium import webdriver
# options = webdriver.FirefoxOptions()
# options.set_headless()
# # options.add_argument(‘-headless‘)
# options.add_argument('--disable-gpu')
# driver=webdriver.Firefox(firefox_options=options)
# driver.get('https://www.zhainanfulishe.net/4955.html')
# driver.get_screenshot_as_file('test.png')
# driver.close()

from selenium import webdriver

browser = webdriver.Firefox()
driver = webdriver.PhantomJS()
driver.set_page_load_timeout(5)
driver.maximize_window()  # 设置全屏
try:
    driver.get("https://juejin.im/post/5ae55861f265da0ba062ec71")
    driver.save_screenshot("./tsm.png")
except Exception as e:
    print(e)

driver.close()
browser.close()
# print(data)
