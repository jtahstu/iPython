"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: test.py
@time: 2017/01/09 16:35
"""

import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import time

url = 'https://movie.douban.com/subject/1292720/comments?status=P'
url = 'https://movie.douban.com/subject/5912992/'
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    , 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
    , 'Host': 'movie.douban.com'
    , 'Referer': 'https://movie.douban.com/top250'
    , 'Upgrade-Insecure-Requests': '1'
    , 'Cache-Control': 'max-age=0'
    , 'Connection': 'keep-alive'
    , 'Accept-Encoding': 'gzip, deflate, br'
    , 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
    ,
           'Cookie': r'll="118196"; bid=evZLAlOEOig; __utma=30149280.19825895.1474635803.1484139127.1484160425.56; __utmz=30149280.1483778648.43.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1921859920.1474635809.1484139127.1484160425.45; __utmz=223695111.1475944004.8.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1484160423%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=9c61c443617ff098.1474635810.45.1484160913.1484143311.; _vwo_uuid_v2=F7FF27DA6C98B9BD15D6F260CC25B989|f1654bdbf661fc84cb743dc31aebfd6e; gr_user_id=9a6c5ff8-a80a-4b91-a715-75f80c10d044; viewed="1054685_26697350"; dbcl2="119273185:REEk8LlBtVY"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.11927; ap=1; ck=puNv; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1484160425; __utmc=30149280; __utmb=223695111.0.10.1484160425; __utmc=223695111; ct=y'}
html = requests.get (url, headers=headers)
print (html.text)
soup = BeautifulSoup (html.text, "html.parser")
# info = soup.select("#info")
# print(info)
