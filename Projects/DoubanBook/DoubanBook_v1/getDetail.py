"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/1/15 16:10
"""
# -*- coding: utf-8 -*-

import json
from pprint import pprint
from Tool import getHtml
from Tool import db
from Tool import readySeries
from Tool import getDateTime


def checkDetailExist(id):
    detail_count = db.db_book_detail.find({'id': id}).count()
    detail_noscore_count = db.db_book_detail_noscore.find({'id': id}).count()
    if detail_count == 0 and detail_noscore_count == 0:
        return False  # 不存在返回false
    return True


def saveBook(book):
    if 'id' not in book.keys():  # 不是有效数据
        pprint(book)
        return
    book['addtime'] = getDateTime()
    if book['rating']['average'] != '0.0':
        db.db_book_detail.insert_one(dict(book))
        print('book id {} is ok , insert into detail'.format(book['id']))
    else:
        db.db_book_detail_noscore.insert_one(dict(book))
        print('book id {} is ok , insert into detail_noscore'.format(book['id']))


def getApi(ids):
    base_url = 'https://api.douban.com/v2/book/'
    for id in ids:
        # if not checkDetailExist(id):  # 数据库不存在
        url = base_url + str(id)
        book = getHtml(url)
        saveBook(json.loads(book))
        # else:
        #     print('book id {} is exist'.format(id))


def getSubjectId():
    res = db.db_book_id.find({}, {'subject_id': 1})
    ready = db.db_book_detail.find({}, {'id': 1})
    ready_noscore = db.db_book_detail_noscore.find({}, {'id': 1})
    ready_ids = []
    for item in ready:
        ready_ids.append(item['id'])
    for item in ready_noscore:
        ready_ids.append(item['id'])
    ids = []
    for item in res:
        ids.append(item['subject_id'])
    return list(set(ids).difference(set(ready_ids)))  # 求差集


def getSeriesID():
    print('get series ids')
    series = db.db_book_detail.find({}, {'series.id': 1})
    series_id = [int(x['series']['id']) for x in series if 'series' in x.keys()]
    series_id = sorted(set(series_id))
    series_ready = getReadySeries()
    return sorted(set(series_id).difference(set(series_ready)))


def getSeriesIdV2():
    print('get series ids v2')
    series_ready = getReadySeries()
    return [i for i in range(1, 40830) if i not in series_ready]


def getReadySeries():
    with open(readySeries, 'r') as ready:
        series_ready = [int(x.strip()) for x in ready.read().split('\n') if x.strip() != '']
    return series_ready


def saveSeriesBook(books):
    if 'books' not in books:
        pprint(books)
        print('save series book faild')
        return
    for book in books['books']:
        saveBook(book)


def getSeriesApi(series_ids):
    base_url = 'https://api.douban.com/v2/book/series/{0}/books?start={1}&count=100'
    for series_id in series_ids:
        with open(readySeries, 'a') as ready:
            ready.write(str(series_id) + '\n')
        json_index = getHtml(base_url.format(series_id, 0))
        json_index = json.loads(json_index)
        if 'total' not in json_index.keys():
            print('series id {0} not exists'.format(series_id))
            pprint(json_index)
            continue
        saveSeriesBook(json_index)
        if json_index['total'] % 100 == 0:
            page = json_index['total'] // 100
        else:
            page = json_index['total'] // 100 + 1
        if page > 1:
            for i in range(1, page):
                url = base_url.format(series_id, str(i * 100))
                book = getHtml(url)
                saveSeriesBook(json.loads(book))


def init():
    ids = getSubjectId()
    getApi(ids)
    # series_ids = getSeriesID()
    # series_ids = getSeriesIdV2()
    # print(len(series_ids))
    # getSeriesApi(series_ids)


if __name__ == "__main__":
    init()
