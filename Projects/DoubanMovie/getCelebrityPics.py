import requests
from bs4 import BeautifulSoup
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
           }

def downPics(url, path):
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    span = soup.select(".mainphoto")
    if len(span) > 0:
        picRealUrl = span[0].img["src"]
        conn = urllib.request.urlopen(picRealUrl)
        file_path = path + os.path.basename(picRealUrl)
        time.sleep(10)
        f = open(file_path, 'wb')
        f.write(conn.read())
        f.close()
        print("{}: save to {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), file_path))


def getPics(url, picPath):
    html = requests.get(url, headers=headers)
    print('get {}'.format(url))
    soup = BeautifulSoup(html.text, "html.parser")
    cover = soup.select(".cover")
    if len(cover) < 5:
        return 'ok'
    s_name = soup.select('#content')[0]
    picPath += s_name.h1.text.strip().replace('的图片', '') + '/'
    if not os.path.isdir(picPath):
        os.mkdir(picPath)
    for i in cover:
        picUrl = i.a["href"]
        downPics(picUrl, picPath)
        time.sleep(10)


c_ids = [1354607, 1349560, 1354586, 1354405, 1354585, 1336623, 1354587, 1354493, 1354593]
for c_id in c_ids:
    for i in range(0, 271, 30):
        try:
            url = 'https://movie.douban.com/celebrity/{}/photos/?type=C&start={}&sortby=like&size=a&subtype=a'.format(
                c_id,
                i)
            getPics(url, picPath='./celebrity/')
        except Exception as e:
            print("错误信息：{0}".format(e))
