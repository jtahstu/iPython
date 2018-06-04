"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/5/30 11:28
"""

from collections import *
from pprint import pprint

Mapping = namedtuple("Mapping",
                     ['FromID', 'ToID', 'Name', 'Site', 'Status', 'EBID', 'NameFrom', 'NameTo', 'LastUpdateTime'])
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


def getMapping():
    mappings = []
    with open("/Users/jtusta/PycharmProjects/iPython/Work/CCA/data/cca_merchant_mapping.csv", 'r',
              encoding='utf-8') as r:
        for line in r.readlines():
            line_split = line.split(',')
            line_split[-1] = line_split[-1].replace('\n', '')
            if (len(line_split) != 9):
                print(line_split)
                continue
            mapping = Mapping._make(line_split)
            mappings.append(mapping)
    return mappings


def init():
    mappings = getMapping()
    mappings = {mapping.Site + str(mapping.FromID): mapping.ToID for mapping in mappings}
    # pprint(mappings)
    mapping_keys = mappings.keys()
    merchants = getData()
    include_sites = ['CSUS', 'CSUK', 'CSAU', 'CSIN', "CSCA"]
    for merchant in merchants:
        if merchant.BCG_SITE.find('|') > 0:
            sites = merchant.BCG_SITE.split('|')
            mids = merchant.BCG_MERID.split('|')

            for (index, site) in enumerate(sites):
                key = sites[index] + str(mids[index])
                if site in include_sites and key in mapping_keys:
                    print("{},{}".format(mappings[key], merchant.Grade))
                    break
        else:
            site = merchant.BCG_SITE
            mid = merchant.BCG_MERID
            key = site + str(mid)
            if site in include_sites and key in mapping_keys:
                print("{},{}".format(mappings[key], merchant.Grade))


if __name__ == "__main__":
    init()
