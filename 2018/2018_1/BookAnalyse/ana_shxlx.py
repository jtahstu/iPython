"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/1/23 15:18
"""
# encoding=utf-8
from collections import Counter
from pprint import pprint

import jieba
import jieba.posseg as psg


def init():
    jieba.enable_parallel(4)
    with open('shxlx.txt', 'rb') as r:
        str = r.read().decode('utf-8')
        segList = psg.cut(str)
        segList = [(x.word.lower(), x.flag) for x in segList if len(x.word) >= 2]
        segCounter = Counter(segList)
        pprint(segCounter.most_common()[0:20])


if __name__ == "__main__":
    init()
