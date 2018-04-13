"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: getBooks.py
@time: 2017/01/13 13:41
"""

import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import time


def getMovies(movieUrl, page):
    html = requests.get(movieUrl)
    soup = BeautifulSoup(html.text, "html.parser")
    items = soup.select(".item")
    count = 0
    for item in items:
        count += 1
        rank = page * 25 + count
        title = item.select(".pl2")[0].a.get('title')
        url = item.select(".pl2")[0].a.get('href')
        pls = item.select(".pl")
        about = pls[0].text.strip()
        rating_num = item.select(".rating_nums")[0].text
        eval_num = pls[1].text.replace('(', '').replace(')', '').strip().replace('人评价', '')
        quote = ""
        if len(item.select(".inq")) > 0:
            quote = item.select(".inq")[0].text.strip()
        connection = pymysql.connect(host='localhost',
                                     user='jtahstu',
                                     password='jtahstu',
                                     db='test',
                                     port=3306,
                                     charset='utf8')
        cursor = connection.cursor()
        sql = 'INSERT into douban_book_top250(rank,detail_url,title,about,rating_num,eval_num,quote) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        cout = cursor.execute(sql, (
            int(rank), url, title, about, float(rating_num), int(eval_num), quote));
        connection.commit()
        cursor.close()
        connection.close()

        print("rank %s : %s , is ok !" % (rank, title))


for i in range(1, 10):
    print("正在抓取第 %d 页" % i)
    movieUrl = "https://book.douban.com/top250?start=" + str(i * 25)
    getMovies(movieUrl, i)
    time.sleep(1)

# 数据库
# CREATE TABLE `douban_book_top250` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `rank` int(11) DEFAULT NULL,
#   `detail_url` varchar(64) DEFAULT NULL,
#   `title` varchar(256) DEFAULT NULL,
#   `about` varchar(256) DEFAULT NULL,
#   `rating_num` int(11) DEFAULT NULL,
#   `eval_num` int(11) DEFAULT NULL,
#   `quote` varchar(256) DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8
