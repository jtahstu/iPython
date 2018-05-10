"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/5/10 21:40
"""
import pymysql
import pymysql.cursors
from pprint import pprint
from phpserialize import *
from collections import Counter


def query(sql):
    connection = pymysql.connect(host='localhost', user='jtahstu', password='jtahstu', db='ifb_base', port=3306,
                                 charset='utf8')
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return data


def init():
    sql = "select PromoFeature from coupon_addinfo where PromoFeature !='' and PromoFeature is not null and PromoFeature!='a:0:{}'"
    features = query(sql)
    kk = []
    for item in features:
        try:
            kk.append(loads(item[0].encode('utf-8')))
        except Exception as e:
            continue
    del features
    keys = [sorted((item.keys())) for item in kk]
    keys_plus = []
    for key, value in enumerate(keys):
        ss = str(value[0], encoding='utf-8')
        for fkey in value[1:]:
            ss += '+' + str(fkey, encoding='utf-8')
        keys_plus.append(ss)
    count = Counter(keys_plus).most_common(255)
    keys_plus_len = len(keys)
    print(keys_plus_len)
    for (k, v) in count:
        print('{}, {}, {}%'.format(k, v, round((v / keys_plus_len) * 100, 3)))


if __name__ == "__main__":
    init()
