"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/5/13 05:27
"""
import pymysql
import pymysql.cursors
from pprint import pprint
import requests
import time


def query(sql):
    connection = pymysql.connect(host='localhost', user='xxx', password='xxx', db='iApp', port=3306,
                                 charset='utf8')
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return data


def getAPI(domain):
    api = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={}".format(domain)
    print("get {}".format(api))
    data = requests.get(url=api).text
    return data


def init():
    domains = query("select id,CONCAT(domain,'.',type) as domain from domain where type='cc' and id>35154")
    for (id, domain) in domains:
        text = getAPI(domain)
        if len(text) > 10 and text.find('210') == -1:
            print("{}".format(text))
            print("id {}, domain {} is not available".format(id, domain))
            with open("./domain_211.txt", 'a') as w:
                w.write(str(id) + ",")
        time.sleep(0.5)


if __name__ == "__main__":
    init()
