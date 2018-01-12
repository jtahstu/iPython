"""
@author: jtusta
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@software: PyCharm Community Edition
@time: 2017/3/25 19:20
"""
import requests
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import time

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    , 'user-agent': 'Mozilla/4.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/40.0'
    , 'Host': 'www.runoob.com'
    , 'Referer': 'http://www.runoob.com/css/css-tutorial.html'
    , 'Upgrade-Insecure-Requests': '1'
    , 'Cache-Control': 'max-age=0'
    , 'Accept-Encoding': 'gzip, deflate, br'
    , 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'}
# requests.adapters.DEFAULT_RETRIES = 5000000
# s = requests.session(config={'keep_alive': False})
def getUrl():
    sql = 'select id,url from spider_course where do=1 and id>11'
    connection = pymysql.connect(host='localhost',
                                 user='jtahstu',
                                 password='',
                                 db='test',
                                 port=3306,
                                 charset='utf8')
    cursor = connection.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    return res

def getHtml(url):
    html = requests.get(url,timeout=30)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, "html.parser")

    return soup

def getContent():
    urls = getUrl()
    for url in urls:
        html = getHtml('http://'+url[1])
        left = html.select('#leftcolumn')
        aa =left[0].find_all('a')

        res =[]

        for a in aa:
            href = ''
            if a["href"].find('www.runoob.com') == -1 :
                href = 'http://www.runoob.com' + a["href"]
            else :
                href = a["href"]
            title = a.text.strip()
            res.append([title,href,url[0]])

        for c in res:
            try:
                url = c[1]
                html = getHtml(url)
                content = html.find(id='content')
                data = [c[2], c[0], content, url]
                saveContent(data)
            except Exception as e:
                print("错误：{0}".format(e))
                continue

            time.sleep(2)


def saveContent(data):
    sql = 'insert into spider_detail(course_id,title,content,url) values(%s,%s,%s,%s)'
    connection = pymysql.connect(host='localhost',
                                 user='jtahstu',
                                 password='',
                                 db='test',
                                 port=3306,
                                 charset='utf8')
    cursor = connection.cursor()
    # print(data)
    count = cursor.execute(sql,(data[0],data[1],str(data[2]),data[3]))
    if count:
        res = 'insert title ' + str(data[1]) + ' ok'
    else:
        res = 'insert title ' + str(data[1]) + ' fail'
    print(res)
    connection.commit()
    cursor.close()
    connection.close()

def init():
    getContent()

if __name__ == "__main__":
    init()
