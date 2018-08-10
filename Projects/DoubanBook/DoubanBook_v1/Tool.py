"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/16 10:10
"""
import random
import time

import requests
from pymongo import MongoClient


def getHtml(url):
    print('{} request url {}'.format(getDateTime(), url))
    # salt = ''.join(random.sample(string.ascii_letters + string.digits, 11))
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'bid=2cTNtmWtjjc',
        'DNT': '1',
        'Host': 'api.douban.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    try:
        html = requests.get(url, headers=headers, timeout=10)
    except Exception as e:
        print(e)
        sleep_sec = random.randrange(600, 1200)
        print('random wait %ds' % (sleep_sec))
        time.sleep(sleep_sec)
        getHtml(url)
    if html.status_code == 404:
        time.sleep(random.randrange(35, 45))
        return '''{
  "msg": "series_not_found",
  "code": 6014,
  "request": "GET /v2/book/series/14/books"
}'''

    if html.status_code != 200:
        sleep_sec = random.randrange(600, 1200)
        print('status_code is %d , error msg is %s , random wait %ds' % (html.status_code, html.text, sleep_sec))
        time.sleep(sleep_sec)
        getHtml(url)  # 递归
    time.sleep(random.randrange(35, 45))
    return html.text


def getDateTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def getDate():
    return time.strftime("%Y-%m-%d", time.localtime())


def md5(str):
    import hashlib
    return hashlib.md5(str.encode("utf-8")).hexdigest()


import platform

if platform.node() == "iZuf69hst5wjxlpnagvjo1Z":
    db = MongoClient('mongodb://jtahstu:jtahstu@127.0.0.1:27017/').iApp
    readySeries = '/root/iPython/Douban/db/readySeries.txt'
else:
    db = MongoClient('mongodb://127.0.0.1:27017/').iApp
    # readySeries = '/Users/jtusta/PycharmProjects/iPython/Test/DoubanBook/db/readySeries.txt'
    readySeries = r'D:\Code\iPython\Projects\DoubanBook\DoubanBook_v1\db\readySeries.txt'
