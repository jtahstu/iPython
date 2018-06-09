"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/5/16 18:58
@des: 由 mapping 关系和初始商家数据，把商家的 grade 加上去
"""
from pprint import pprint
# from sys import path
# path.append('./')

import pymysql
import pymysql.cursors


def query(sql):
    connection = pymysql.connect(host='localhost', user='jtahstu', password='jtahstu', db='ice_base', port=3306,
                                 charset='utf8')
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return data


def getData():
    status = []
    with open("./data/ice_mercahnts.csv", 'r') as r:
        for line in r.readlines():
            line_split = line.split('\t')
            status.append({'sites': line_split[0], 'mids': line_split[1], 'grade': line_split[2].replace('\n', '')})
    return status


def init():
    mappings = query("select Site,FromID,ToID from merchant_mapping where Status='Active' limit 10000")
    # pprint(mappings[0:5])
    map_mid = {bcg_site + str(bcg_id): mid for (bcg_site, bcg_id, mid) in mappings}
    map_mid_keys = map_mid.keys()
    # pprint(map_mid)
    merchants = getData()
    # pprint(merchants[0:5])
    # exit(-1)
    include_sites = ['CSUS', 'CSUK', 'CSAU', 'CSIN', "CSCA"]
    for merchant in merchants:
        if merchant['sites'].find('|') > 0:
            sites = merchant['sites'].split('|')
            mids = merchant['mids'].split('|')

            for (index, site) in enumerate(sites):
                key = sites[index] + str(mids[index])
                if site in include_sites and key in map_mid_keys:
                    print("{},{}".format(map_mid[key], merchant['grade']))
                    break
        else:
            site = merchant['sites']
            mid = merchant['mids']
            key = site + str(mid)
            if site in include_sites and key in map_mid_keys:
                print("{},{}".format(map_mid[key], merchant['grade']))


if __name__ == "__main__":
    init()
