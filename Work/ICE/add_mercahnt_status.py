"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/5/13 04:02
@des: ice 首批上线商家3469个，有的商家是多语言的,把CSDE/CSFR,非英语去掉，如果还是多，取第一个
        ./data/ice_mercahnt_status.csv 就是要上线的商家列表
"""

from pprint import pprint


def getData():
    status = []
    with open("./data/ice_mercahnt_status.csv", 'r') as r:
        for line in r.readlines():
            line_split = line.split('\t')
            if line_split[0].find('|') > 0:
                status.append({'sites': line_split[0], 'mids': line_split[1].replace('\n', '')})
    return status


def init():
    status = getData()
    # pprint(status)
    for item in status:
        sites = item['sites'].split('|')
        mids = item['mids'].split('|')
        include_sites = ['CSUS', 'CSUK', 'CSAU', 'CAIN']
        for (index, site) in enumerate(sites):
            if site in include_sites:
                print("{},{}".format(sites[index], mids[index]))
                break


if __name__ == "__main__":
    init()
