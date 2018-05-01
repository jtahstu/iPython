"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/15 11:14
"""
import string
import random

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time
import pymongo
from datetime import datetime

db = MongoClient('mongodb://jtahstu:jtahstu@127.0.0.1:27017/').iApp
#db = MongoClient('mongodb://127.0.0.1:27017/').iApp


def getHtml(url):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 11))
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': 'bid=' + salt ,
        'DNT': '1',
        'Host': 'book.douban.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/527.36 (KHTML, like Gecko) Chrome/60.0.3239.132 Safari/527.36'
    }
    # proxies = [
    #     "101.53.101.172:9999","171.117.93.229:8118","119.251.60.37:21387","58.246.194.70:8080",
    #     "115.173.218.224:9797","110.77.0.70:80"
    # ]
    html = requests.get(url, headers=headers)
    if html.status_code != 200:
        print('status_code is %d' % html.status_code)
        quit(0)
    return html.text


def getDateTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def getTagsFromUrl():
    url = "https://book.douban.com/tag/?icn=index-nav"
    html = getHtml(url)
    soup = BeautifulSoup(html, "lxml")  # 解析网页信息
    tags = soup.select("#content > div > div.article > div > div > table > tbody > tr > td > a")
    urls = []
    for tag in tags:
        tag = tag.get_text()  # 将列表中的每一个标签信息提取出来
        url = "https://book.douban.com/tag/" + str(tag)
        urls.append(url)
    for index, url in enumerate(urls):
        item = {
            'id': index + 1,
            'tag_url': url,
            'tag_name': url.replace('https://book.douban.com/tag/', ''),
            'status': 1,
            'updated_at': getDateTime(),
            'crawl_count': 0,
            'page': 0
        }
        res = db.douban_tag.insert_one(item)
        print(res)
    # return urls


def getTagsFromDB():
    return db.db_book_tag.find({'status': 1}) \
        .sort([('id', pymongo.ASCENDING)])


def getSubjectId(url, page):
    url += '?start=' + str((page - 1) * 20) + '&type=T'
    print(url)
    html = getHtml(url)
    soup = BeautifulSoup(html, "html.parser")  # 解析网页信息
    subjects = soup.select("#subject_list > ul.subject-list > li.subject-item > div.info > h2 > a")
    if len(subjects) == 0:
        return []
    ids = []
    for subject in subjects:
        href = subject.get('href')
        id = href.replace('https://book.douban.com/subject/', '').replace('/', '')
        ids.append(id)
    return ids


def saveId(tag, page, ids):
    tag_id = tag['id']
    for id in ids:
        item = {
            'tag_id': tag_id,
            'subject_id': id
        }
        db.db_book_id.insert_one(item)
    tag['updated_at'] = getDateTime()
    if len(ids) > 0:
        tag['page'] = page
    updateTag(tag)


def setStatus(tag):
    tag['status'] = 0
    updateTag(tag)


def updateTag(tag):
    db.db_book_tag.update({'_id': tag['_id']}, {"$set": tag})


if __name__ == "__main__":
    getPages = 100
    tags = getTagsFromDB()
    for tag in tags:
        print(tag)
        if tag['page'] == 1:
            tag['page'] = 0
        for page in range(tag['page'] + 1, getPages + 1):
            ids = getSubjectId(tag['tag_url'], page)
            if len(ids) == 0:
                setStatus(tag)
                break
            print(ids)
            saveId(tag, page, ids)
            time.sleep(int(random.uniform(25, 35)))
