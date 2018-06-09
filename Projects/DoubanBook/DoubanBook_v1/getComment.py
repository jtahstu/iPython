"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/2/7 10:24
"""

import json
from pprint import pprint
import Tool
import pymongo


def getBookID():
    ids = [int(i['id']) for i in Tool.db.db_book_detail.find({"rating.numRaters": {"$gt": 5000}}, {'id': 1}).sort(
        [("rating.numRaters", pymongo.DESCENDING)])]
    print('here are need crawl count ', len(ids))
    return ids


def getComment(url):
    soup = Tool.getBS(url)
    lis = soup.select('li.comment-item')
    for li in lis:
        item = {}
        item['comment'] = li.select('p.comment-content')[0].text.strip()
        print(item)


def init():
    # bookIDs = getBookID()
    bookIDs = [1770782, 25862578]
    for id in bookIDs:
        comments = getComment('https://book.douban.com/subject/{}/comments/'.format(id))
        res = Tool.db.db_book_comment.insertMany(comments)
        print(res)


if __name__ == "__main__":
    init()
