"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: beautyleg.py
@time: 2017/01/15 21:54
"""
import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import urllib.request
import os
import time

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    , 'user-agent': 'Mozilla/4.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/40.0'
    , 'Host': 'www.beautyleg.com'
    , 'Upgrade-Insecure-Requests': '1'
    , 'Cache-Control': 'max-age=0'
    , 'Connection': 'keep-alive'
    , 'Accept-Encoding': 'gzip, deflate, br'
    , 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
           }


def downPics(url, path, rank, count):
    try:
        conn = urllib.request.urlopen (url, timeout=5)
        f = open (path, 'wb')
        f.write (conn.read ())
        f.close ()
        conn.close()
        print ("下载 page " + str (rank) + " 的第 " + str (count) + " 张图片 ok ! " + time.asctime ())
    except Exception as e:
        print (e)
        print ("{} 下载失败 !".format (url))
        return


def getPics(url, page):
    html = requests.get (url, timeout=10)
    soup = BeautifulSoup (html.text, "html.parser")
    all = soup.select (".table_all")
    imgs = all[0].select ("td")
    count = 0
    picPath = '/Users/jtusta/PycharmProjects/Python/Test1.0/spider/' + str (page)
    if not os.path.isdir (picPath) and not os.path.exists (picPath):
        os.mkdir (picPath)
    for i in imgs:
        try:
            picUrl = i.a['href']
            count += 1
            name = str (count) + ".jpg"
            picPathSave = picPath + "\\" + name
            if os.path.exists (picPathSave):
                continue
            downPics (picUrl, picPathSave, page, count)
        except Exception as e:
            print (e)
            print ("第 {} 页 第 {} 张下载失败 ! {}".format (page, count, time.asctime ()))
            continue


for i in range (84, 93):
    try:
        print ("正在下载第 {} 页 !".format (i))
        url = "http://www.beautyleg.com/photo/show.php?no=" + str (i)
        print (url)
        getPics (url, i)
    except Exception as e:
        print (e)
        print ("第 {} 页下载失败 !".format (i))
        continue
    time.sleep(3)
