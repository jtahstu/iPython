"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: requests1.0.py
@time: 2017/01/08 12:49
"""
import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import time


def getMovies(movieUrl):
    html = requests.get(movieUrl)
    soup = BeautifulSoup(html.text, "html.parser")
    items = soup.select(".item")
    for item in items:
        # 排名
        rank = item.em.text
        # 详情页
        detailUrl = item.a.get("href")
        # 标题
        titles = item.select(".title")
        title = titles[0].text.strip()
        title2 = ""
        if len(titles) > 1:
            title2 = item.select(".title")[1].text.strip().replace("/","")
        titleOther = item.select(".other")[0].text.strip().replace("/","")
        bd = item.p.text.strip().split("\n")
        # 人物
        people = bd[0].strip()
        # 类型
        type = bd[1].strip()
        # 评分
        ratingNum = item.select(".star span")[1].text
        # 评价数
        evalNum = item.select(".star span")[3].text.replace("人评价", "")
        # 引述
        quote = item.select(".inq")[0].text.strip()

        connection = pymysql.connect(host='localhost',
                                     user='xxx',
                                     password='xxx',
                                     db='python',
                                     port=3306,
                                     charset='utf8')
        cursor = connection.cursor()
        sql = 'INSERT into douban_movie_top250(rank,detail_url,title,title2,title_other,people,type,rating_num,eval_num,quote) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cout = cursor.execute(sql, (
        int(rank), detailUrl, title, title2, titleOther, people, type, float(ratingNum), int(evalNum), quote));
        connection.commit()
        cursor.close()
        connection.close()

        print("rank %s : %s , is ok !" % (rank, title))


for i in range(0, 10):
    print("正在抓取第 %d 页" % i)
    movieUrl = "https://movie.douban.com/top250?start=" + str(i * 25)
    getMovies(movieUrl)
    time.sleep(2)

