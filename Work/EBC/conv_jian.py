#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/8/28 15:47

from hanziconv import HanziConv
import os


def init():
    file_path = '/Users/jtusta/PycharmProjects/iPython/Work/EBC/file/'
    file_out_path = '/Users/jtusta/PycharmProjects/iPython/Work/EBC/file_out/'
    files = os.listdir(file_path)
    for file in files:
        # if not file.endswith('sql'):
        #     continue
        with open(file_path + file, encoding='utf-8', mode='r') as r:
            codes = r.readlines()
            print(len(codes))

        with open(file_out_path + file, encoding='utf-8', mode='a') as w:
            for line in codes:
                xx = HanziConv.toTraditional(line)
                w.write(xx)
    # print(HanziConv.toTraditional('免费[CATEGORYNAME]优惠码，折扣活动 | [SITENAME]'))

if __name__ == '__main__':
    init()
