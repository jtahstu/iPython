"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/5/29 14:02
@des: cca 首批上线商家3486个，有的商家是多语言的,把CSDE/CSFR,非英语去掉，如果还是多，取第一个
        ./data/cca_merchants.csv 就是要上线的商家列表
"""

from pprint import pprint
from collections import *

Merchant = namedtuple('Merchant',
                      ['NAME', 'BCG_SITE', 'BCG_MERID', 'SESSION_60D', 'REVENUE_60D', 'MAPPING_STATUS', 'URL',
                       'PAGE_CNT', 'AFF_PAGE_CNT', 'Search_Volumn', 'Remark', 'Grade'])


def getData():
    merchants = []
    with open("/Users/jtusta/PycharmProjects/iPython/Work/CCA/data/cca_merchants.csv", 'r', encoding='utf-8') as r:
        for line in r.readlines():
            line_split = line.split(',')
            line_split[-1] = line_split[-1].replace('\n', '')
            if (len(line_split) != 12):
                print(line_split)
                continue
            merchant = Merchant._make(line_split)
            merchants.append(merchant)
    return merchants


def init():
    merchants = getData()
    pprint(merchants[0])
    for merchant in merchants:
        sites = merchant.BCG_SITE.split('|')
        mids = merchant.BCG_MERID.split('|')
        include_sites = ['CSUS', 'CSUK', 'CSAU', 'CSIN', 'CSCA']
        with open('/Users/jtusta/PycharmProjects/iPython/Work/CCA/data/cca_mapping_status.csv', 'a', encoding='utf-8') as w:
            for (index, site) in enumerate(sites):
                if site in include_sites:
                    line = "{},{}\n".format(sites[index], mids[index])
                    w.write(line)
                    break


if __name__ == "__main__":
    init()
