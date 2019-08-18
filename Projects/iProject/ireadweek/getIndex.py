"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@software: PyCharm
@time: 2017/6/29 13:20
"""

import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import time

def getBookList(url,i):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    title = soup.select(".hanghang-za-title")[0].text.strip()
    if(title==''):
        return
    content = soup.select('.hanghang-shu-content-font')[0].find_all('p')
    author = content[0].text.replace("作者：", "").strip()
    classify = content[1].text.replace("分类：", "").strip()
    des = content[5].text.strip()
    print(len(content))
    if len(content)>=7:
        des2 = content[6].text.strip()
        des = des + '\n' + des2
    url = soup.select('.downloads')[0].get("href")
    saveBooks(title,author,classify,des,url,i)
    print(title,author,classify)
    # print(author)
    # print(classify)
    # print(des)
    print(url)

def saveBooks(title,author,classify,des,url,i):
    connection = pymysql.connect(host='localhost',
                                 user='xxx',
                                 password='xxx',
                                 db='spider',
                                 port=3306,
                                 charset='utf8')
    cursor = connection.cursor()
    sql = 'INSERT into books(title,author,classify,des,url) VALUES(%s,%s,%s,%s,%s)'
    # print(sql % (title, author, classify, des, url));
    cout = cursor.execute(sql, (
        title, author, classify, des, url))
    connection.commit()
    cursor.close()
    connection.close()
    if cout:
        print("第 %d 篇ok" % i)

list = []
for i in range(9000, 9010):
    print("正在抓取第 %d 篇" % i)
    url = "http://www.ireadweek.com/index.php/bookInfo/" + str(i) + ".html"
    # print(url)
    try:
        getBookList(url,i)
    except:
        list.append(i)
        print('第 ' + str(i) + ' 抓取异常')
        continue
print(list)