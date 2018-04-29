import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors

indexUrl = 'http://www.runoob.com/'

def getSubjects():

    html = requests.get(indexUrl)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, "html.parser")
    items = soup.select(".item-1")
    return items

def insertTable(row):
    sql = 'insert into spider_course(id,url,title,introduce) values(%s,%s,%s,%s)'
    connection = pymysql.connect(host='localhost',
                                 user='jtahstu',
                                 password='',
                                 db='test',
                                 port=3306,
                                 charset='utf8')
    cursor = connection.cursor()
    res = cursor.execute(sql,(row[0],row[1],row[2],row[3]))
    if res:
        print('id:{0},{1}插入成功'.format(row[0],row[2]))
    connection.commit()
    cursor.close()
    connection.close()

def showItems():
    items = getSubjects()
    i = 0
    for item in items:
        i += 1
        try:
            href = item['href']
            title = item.h4.text.replace(' ','').replace('【','').replace('】','').replace('学习','')
            introduce = item.strong.text
            data = [i,href,title,introduce]
            insertTable(data)
        except Exception as e:
            print("错误信息：{0}".format(e))
            continue

showItems()
