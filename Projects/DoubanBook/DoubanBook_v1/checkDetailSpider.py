"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/2/5 10:11
"""
from _md5 import md5

import Tool
from pprint import pprint
import os
import time
import requests


def get2DBCount():
    detail_count_now = Tool.db.db_book_detail.find({}, {'_id': 1}).count()
    detail_noscore_count_now = Tool.db.db_book_detail_noscore.find({}, {'_id': 1}).count()
    return detail_count_now, detail_noscore_count_now


def checkDetailCount():
    pprint([Tool.getDateTime(), 'checkDetailCount start'])
    counts = [x for x in Tool.db.temp.find({'type': 'db_detail_count'})]
    for count in counts:
        if count['flag'] == 'detail_count':
            detail = dict(count)
        else:
            detail_noscore = dict(count)
    detail_count_now, detail_noscore_count_now = get2DBCount()
    detail['count'] = detail_count_now
    detail['update_time'] = Tool.getDateTime()
    detail_noscore['count'] = detail_noscore_count_now
    detail_noscore['update_time'] = Tool.getDateTime()
    Tool.db.temp.update({'_id': detail['_id']}, {"$set": dict(detail)})
    Tool.db.temp.update({'_id': detail_noscore['_id']}, {"$set": dict(detail_noscore)})
    if checkCurrentScript():
        pprint([Tool.getDateTime(), 'nice , script is ok', detail, detail_noscore])
    else:
        pprint([Tool.getDateTime(), 'Warning, the script may perform an error'])
        autorun()


def checkCurrentScript():
    times = 3
    detail_before, detail_noscore_before = get2DBCount()
    for i in range(1, times + 1):
        time.sleep(100)
        detail_now, detail_noscore_now = get2DBCount()
        if detail_now != detail_before or detail_noscore_now != detail_noscore_before:
            return True
        detail_before = detail_now
        detail_noscore_before = detail_noscore_now
    return False


def autorun():
    pprint([Tool.getDateTime(), 'autorun script start'])
    mail = {
        'msg': Tool.getDateTime() + u'  豆瓣爬虫脚本貌似不正常，已重新启动',
        'toUser': 'root@jtahstu.com',
        'verify': Tool.md5('jtahstu' + Tool.getDate())
    }
    json = requests.get('https://i.jtup.cc/api/mail', params=mail)
    pprint(json)
    os.system('python3 /root/iPython/Douban/getDetail.py >> /root/iPython/Douban/checkDetailSpider.log')


def init():
    checkDetailCount()


if __name__ == "__main__":
    init()
