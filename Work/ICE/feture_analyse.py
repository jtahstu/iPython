"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/5/10 21:40
@des: 分析了下 coupon_addinfo PromoFeature 字段 key 值分布，分析结果在 doc 里
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


def getAllValidFeatures():
    sql = "select ca.PromoFeature from coupon c left join coupon_addinfo ca on c.ID=ca.ID where ca.PromoFeature !='' and ca.PromoFeature is not null and ca.PromoFeature!='a:0:{}' and c.Status='Active' limit 1000000"
    features = query(sql)
    all_valid_features = []
    for item in features:
        try:
            all_valid_features.append(loads(item[0].encode('utf-8')))
        except Exception as e:
            continue
    return all_valid_features


def getKeyDistribution():
    all_valid_features = getAllValidFeatures()
    keys = [sorted(list(item.keys())) for item in all_valid_features]
    exclude = [b'scope', b'site_wide']
    keys_d = [list(set(k).difference(set(exclude))) for k in keys if list(set(k).difference(set(exclude)))]
    keys_plus = []
    for key, value in enumerate(keys_d):
        ss = str(value[0], encoding='utf-8')
        for fkey in value[1:]:
            ss += '+' + str(fkey, encoding='utf-8')
        keys_plus.append(ss)
    count = Counter(keys_plus).most_common(255)
    keys_plus_len = len(keys)
    print(keys_plus_len)
    for (k, v) in count:
        print('{}, {}, {}%'.format(k, v, round((v / keys_plus_len) * 100, 3)))


def getPercentDistribution():
    all_valid_features = getAllValidFeatures()
    values = [item[b'percent'][b'scope'] for item in all_valid_features if
              b'percent' in list(item.keys()) and b'scope' in list(item[b'percent'].keys())]
    count = Counter(values).most_common(255)
    values_len = len(values)
    print(values_len)
    for (k, v) in count:
        print('{}, {}, {}%'.format(k, v, round((v / values_len) * 100, 3)))


def getScopeDistribution():
    all_valid_features = getAllValidFeatures()
    values = [item[b'scope'][b'name'] for item in all_valid_features if
              b'scope' in list(item.keys()) and b'name' in list(item[b'scope'].keys())]
    count = Counter(values).most_common(255)
    values_len = len(values)
    print(values_len)
    for (k, v) in count:
        print('{}, {}, {}%'.format(k, v, round((v / values_len) * 100, 3)))


def getProductDistribution():
    all_valid_features = getAllValidFeatures()
    values = [item for item in all_valid_features if list(item.keys()) == [b'product', b'scope']]
    pprint(values[0:20])


if __name__ == "__main__":
    getKeyDistribution()
    # getPercentDistribution()
    # getScopeDistribution()
    # getProductDistribution()
