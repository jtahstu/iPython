#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/9/10 18:20

import json
from selenium import webdriver
import os
from urllib.parse import urlparse

def getSeleniumBrowser(url, display=True):

    chrome_options = webdriver.ChromeOptions()
    if display is False:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)

    # firefox_options = webdriver.FirefoxOptions()
    # if display is False:
    #     firefox_options.add_argument('--headless')
    #     firefox_options.add_argument('--disable-gpu')
    # browser = webdriver.Firefox(firefox_options=firefox_options)

    browser.implicitly_wait(5)
    browser.set_window_size(1920, 1080)
    # browser.maximize_window()
    try:
        browser.get(url)
        return browser
    except:
        print('getSeleniumBrowser: get faild , {}'.format(url))
        return False

def screen(browser, id):
    file_path = './image/{}.png'.format(id)
    browser.get_screenshot_as_file(file_path)
    print('save to {}'.format(file_path))
    # js = "document.documentElement.scrollTop=10000"
    # browser.execute_script(js)
    # browser.get_screenshot_as_file(file_path + "_footer.png")
    browser.quit()

def init():
    with open('url.json','r') as r:
        urls = json.loads(r.read())
    for id,url in enumerate(urls):
        if os.path.exists('./image/{}.png'.format(id)):
            continue
        try:
            browser = getSeleniumBrowser(url['OriginalUrl'], display=True)
            print('get {}'.format(url))
            screen(browser, id)
            browser.quit()
        except Exception as e:
            print(e)
            print("{} has contnue".format(id))
            continue


if __name__ == '__main__':
    init()