"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: getMoviesDetail.py
@time: 2017/01/09 14:16
"""

import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import time


def db(type, rank, detail=[]):
    res = ""
    connection = pymysql.connect(host='localhost',
                                 user='jtahstu',
                                 password='jtahstu',
                                 db='python',
                                 port=3306,
                                 charset='utf8')
    cursor = connection.cursor()
    if type == 1:
        sql = 'select detail_url from douban_movie_top250 where rank=%s'
        cursor.execute(sql, (str(rank)));
        res = cursor.fetchone()[0]
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
    url = db(1, rank)
    return url


def saveDetail(rank, detail):
    res = db(2, rank, detail)
    return res


def getDetail(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        , 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        , 'Host': 'movie.douban.com'
        , 'Referer': 'https://movie.douban.com/top250'
        , 'Upgrade-Insecure-Requests': '1'
        , 'Cache-Control': 'max-age=0'
        , 'Connection': 'keep-alive'
        , 'Accept-Encoding': 'gzip, deflate, br'
        , 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    info = soup.select("#info")
    infos = info[0].text.split("\n")
    director = infos[1].replace("导演:", "").strip()
    screenwriter = infos[2].replace("编剧:", "").strip()
    starring = infos[3].replace("主演:", "").strip()
    type = infos[4].replace("类型:", "").strip()
    location = infos[5].replace("制片国家/地区:", "").strip()
    language = infos[6].replace("语言:", "").strip()
    reltime = infos[7].replace("上映日期:", "").strip()
    len = infos[8].replace("片长:", "").strip()
    othernames = infos[9].replace("又名:", "").strip()
    imdb = infos[10].replace("IMDb链接:", "").strip()

    introduceAll = soup.select(".all")
    if introduceAll:
        introduce = introduceAll[0].text.strip()
    else:
        introduce = soup.select("#link-report")
        introduce = introduce[0].text.replace("©豆瓣", "").strip()
    list = [director, screenwriter, starring, type, location, language, reltime, len, othernames, imdb, introduce]
    return list


list = [22, 30]
for i in range(100, 251):
    # for i in list:
    print("正在抓取rank %d" % i)
    try:
        url = getUrl(i)
        detail = getDetail(url)
        res = saveDetail(i, detail)
        print(res)
        time.sleep(1)
    except:
        list.append(i)
        print('rank ' + str(i) + ' 抓取异常')
        continue

print("抓取完毕，以下rank抓取失败：")
print(list)
# [22, 30, 110, 131, 237]
# 这些出错的都是404错误，实际上页面是存在的，这5个就不弄了
