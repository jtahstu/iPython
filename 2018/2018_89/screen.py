#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/9/10 18:20

def getSeleniumBrowser(url, display=True):
    from selenium import webdriver
    # chrome_options = webdriver.ChromeOptions()
    # if display is False:
    #     chrome_options.add_argument('--headless')
    #     chrome_options.add_argument('--disable-gpu')
    # browser = webdriver.Chrome(chrome_options=chrome_options)

    firefox_options = webdriver.FirefoxOptions()
    if display is False:
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
    browser = webdriver.Firefox(firefox_options=firefox_options)

    browser.implicitly_wait(5)
    browser.set_window_size(1920, 1080)
    # browser.maximize_window()
    try:
        browser.get(url)
        return browser
    except:
        print('getSeleniumBrowser: get faild , {}'.format(url))
        return False

def screen(url, browser):
    from urllib.parse import urlparse
    o = urlparse(url)
    file_path = './' + o.netloc.replace('www.', '')
    browser.get_screenshot_as_file(file_path + "_header.png")
    print('save to {}'.format(file_path))
    js = "document.documentElement.scrollTop=10000"
    browser.execute_script(js)
    browser.get_screenshot_as_file(file_path + "_footer.png")
    browser.quit()

def init():
    urls = ['https://www.anycodes.com/']
    for url in urls:
        browser = getSeleniumBrowser(url, display=True)
        print('start screen')
        screen(url, browser)
        browser.quit()


if __name__ == '__main__':
    init()