"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: getMoviesPics.py
@time: 2017/01/11 20:53
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
    , 'Host': 'movie.douban.com'
    , 'Referer': 'https://movie.douban.com/subject/1292720/'
    , 'Upgrade-Insecure-Requests': '1'
    , 'Cache-Control': 'max-age=0'
    , 'Connection': 'keep-alive'
    , 'Accept-Encoding': 'gzip, deflate, br'
    , 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
    ,
           'Cookie': r'll="118196"; bid=evZLAlOEOig; __utma=30149280.19825895.1474635803.1484139127.1484160425.56; __utmz=30149280.1483778648.43.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1921859920.1474635809.1484139127.1484160425.45; __utmz=223695111.1475944004.8.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1484160423%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=9c61c443617ff098.1474635810.45.1484160913.1484143311.; _vwo_uuid_v2=F7FF27DA6C98B9BD15D6F260CC25B989|f1654bdbf661fc84cb743dc31aebfd6e; gr_user_id=9a6c5ff8-a80a-4b91-a715-75f80c10d044; viewed="1054685_26697350"; dbcl2="119273185:REEk8LlBtVY"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.11927; ap=1; ck=puNv; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1484160425; __utmc=30149280; __utmb=223695111.0.10.1484160425; __utmc=223695111; ct=y'}


def db(type, rank, detail=[]):
    res = ""
    connection = pymysql.connect(host='localhost',
                                 user='xxx',
                                 password='xxx',
                                 db='python',
                                 port=3306,
                                 charset='utf8')
    cursor = connection.cursor()
    if type == 1:
        sql = 'select detail_url,title from douban_movie_top250 where rank=%s'
        cursor.execute(sql, (str(rank)));
        res = cursor.fetchone()
    elif type == 2:
        sql = 'insert into douban_movie_top250_details(rank,dirsctor, screenwriter, starring, type, location, language, rel_time, len, other_names, imdb, introduce)' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        count = cursor.execute(sql, (
            rank, detail[0], detail[1], detail[2], detail[3], detail[4], detail[5], detail[6], detail[7], detail[8],
            detail[9], detail[10]))
        if count:
            res = 'insert rank ' + str(rank) + ' ok'
        else:
            res = 'insert rank ' + str(rank) + ' fail'
    connection.commit()
    cursor.close()
    connection.close()
    return res


def getUrl(rank):
    res = db(1, rank)
    return res[0]


def getTitle(rank):
    res = db(1, rank)
    return res[1]


def downPics(url, path, rank, count):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    span = soup.select(".mainphoto")
    if len(span) > 0:
        picRealUrl = span[0].img["src"]
        conn = urllib.request.urlopen(picRealUrl)
        f = open(path, 'wb')
        f.write(conn.read())
        f.close()
        print("下载 rank " + str(rank) + " 的第 " + str(count) + " 张图片 ok !")


def getPics(url, rank, page):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    cover = soup.select(".cover")
    count = 0
    picPath = 'C:\\Users\\jtahstu\\Desktop\\DoubanTop250Pics\\' + str(rank) + " " + getTitle(rank)
    if not os.path.isdir(picPath):
        os.mkdir(picPath)
    for i in cover:
        picUrl = i.a["href"]
        count += 1
        countt = count + (page - 1) * 40
        name = str(countt) + ".jpg"
        picPathSave = picPath + "\\" + name
        downPics(picUrl, picPathSave, rank, countt)
        time.sleep(1)


rank = 250
pages = 5
for rank in range(153, rank + 1):
    print("正在抓取rank %d" % rank)
    for page in range(1, pages + 1):
        try:
            url = getUrl(rank) + "photos?type=S&start=" + str((page - 1) * 40) + "&sortby=vote&size=a&subtype=a"
            getPics(url, rank, page)
        except Exception as e:
            print("错误信息：{0}".format(e))
            print("抓取 rank %d 的第 %d 页图片失败 ！" % (rank, page))
            continue
