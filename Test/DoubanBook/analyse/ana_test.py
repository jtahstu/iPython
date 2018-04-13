"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/1/18 15:29
"""
from pprint import pprint

import pandas as pd
import numpy as np
from collections import Counter
import sys

sys.path.append('../')
import Tool


def calcCrawlCount():
    rid = Tool.db.db_book_detail.find({}, {'id': 1})
    ready_ids = set([i['id'] for i in rid])
    aid = Tool.db.db_book_id.find({}, {'subject_id': 1})
    all_ids = set([j['subject_id'] for j in aid])
    print('已爬取的数量和总数', len(ready_ids), len(all_ids))
    print('未爬取的数量', len(all_ids.difference(ready_ids)))
    print('比 id 库多爬取的数量', len(ready_ids.difference(all_ids)))


def scoreDescribe():
    datas = Tool.db.db_book_detail.find({}, {'rating.average': 1, 'publisher': 1, 'series': 1})
    datas = [y for y in datas]
    scores = [float(score['rating']['average']) for score in datas]
    scores = np.array(scores)
    s = pd.DataFrame(scores)
    print(s.describe())


def test():
    datas = Tool.db.db_book_detail.find({}, {'rating.average': 1, 'publisher': 1, 'series': 1})
    datas = [y for y in datas]
    publisher = [x['publisher'] for x in datas if 'publisher' in x.keys()]
    p = Counter(publisher)
    # pprint(p.most_common()[0:20])

    series_id = [x['series']['title'] for x in datas if 'series' in x.keys()]
    s = Counter(series_id)
    # pprint(s.most_common()[0:20])


def init():
    # test()
    # scoreDescribe()
    calcCrawlCount()


if __name__ == "__main__":
    init()
