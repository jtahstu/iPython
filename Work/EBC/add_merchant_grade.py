"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/6/4 14:20
"""
from collections import *
from pprint import pprint


def init():
    cca_mers = {}
    with open('/Users/jtusta/PycharmProjects/iPython/Work/EBC/data/cca_mer_add_2018-6-4.csv', 'r',
              encoding='utf-8') as r:
        for line in r.readlines():
            fromid, country, grade, _ = line.split(',')
            country = 'CS' + country
            cca_mers[country + fromid] = chr(int(grade)-1+ord('A'))
        # pprint(cca_mers)
    ebc_mers = {}
    with open('/Users/jtusta/PycharmProjects/iPython/Work/EBC/data/ebc_mer_add_2018-6-4.csv', 'r',
              encoding='utf-8') as r:
        for line in r.readlines():
            fromid, site, mid = line.split(',')
            mid = (mid.replace('\n', ''))
            ebc_mers[site + fromid] = mid
        # pprint(ebc_mers)
    for key in ebc_mers.keys():
        print(ebc_mers[key] + ',' + cca_mers[key])


if __name__ == "__main__":
    init()
