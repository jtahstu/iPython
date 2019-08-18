#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu-PC
# Software: PyCharm
# Time: 2019-08-17 23:06
# Description: todo list


import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import urllib.request
import os
import time
from pprint import pprint

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    , 'user-agent': 'Mozilla/4.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/60.0'
    , 'Host': 'www.kunv.cc'
    , 'Upgrade-Insecure-Requests': '1'
    , 'Cache-Control': 'max-age=0'
    , 'Connection': 'keep-alive'
    , 'Accept-Encoding': 'gzip, deflate, br'
    , 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
           }


def downPics(url, path):
    try:
        conn = urllib.request.urlopen(url, timeout=5)
        f = open(path, 'wb')
        f.write(conn.read())
        f.close()
        conn.close()
        print("下载 " + url + " ok ! " + time.asctime())
    except Exception as e:
        print(e)
        print("{} 下载失败 !".format(url))
        return


def getPics(url):
    html = requests.get(url, timeout=10)
    html.encoding = 'UTF-8'
    soup = BeautifulSoup(html.text, "html.parser")
    title = soup.select(".weizhi>h1")[0].text.strip()
    pic_url = soup.select("#img_view>img")[0].get("src")
    pic_url = domain + pic_url
    pprint([title, pic_url])

    picPath = 'E:\\source\\kunv.cc\\' + str(title)
    if not os.path.isdir(picPath) and not os.path.exists(picPath):
        os.mkdir(picPath)
    else:
        print("{} has download".format(title))
        return False

    picPathSave = picPath + "\\1.jpg"
    downPics(pic_url, picPathSave)

    all_pages = soup.select("#pages>a")
    if len(all_pages) is 0:
        print(url + " no image")
        return False

    for page in all_pages:
        link = page.get("href")
        if link is not None:
            file_name = link.replace('.html', '') + ".jpg"
            link = main_url + link
            print(link)
            # continue
            try:
                html = requests.get(link, timeout=10)
                html.encoding = 'UTF-8'
                soup = BeautifulSoup(html.text, "html.parser")
                pic_url = soup.select("#img_view>img")
                print(pic_url)
                pic_url = pic_url[0].get("src")
                pic_url = domain + pic_url
                picPathSave = picPath + "\\" + file_name
                downPics(pic_url, picPathSave)
            except Exception as e:
                print(e)
                continue



def getList(url):
    html = requests.get(url, timeout=10)
    soup = BeautifulSoup(html.text, "html.parser")
    all = soup.select(".img")
    links = all[0].select("li")

    all_links = []
    for i in links:
        link = i.a['href']
        all_links.append(domain + link)

    pprint(all_links)
    return all_links


main_url = 'http://www.kunv.cc/ligui/'
domain = 'http://www.kunv.cc'
for i in range(1, 19):
    if i == 1:
        url = main_url
    else:
        url = "http://www.kunv.cc/ligui/17-{}.html".format(i)
    # print(url)
    links = getList(url)
    # links = ['http://www.kunv.cc/ligui/2876.html']

    for link in links:
        # getPics(link)
        try:
            print(link)
            getPics(link)
        except Exception as e:
            print(e)
            continue
        time.sleep(1)
