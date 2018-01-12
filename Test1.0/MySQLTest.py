"""
@author: jtusta
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@software: PyCharm Community Edition
@time: 2017/3/25 17:12
"""
import pymysql
import pymysql.cursors


def init():
    connection = pymysql.connect(host='localhost',
                                 user='jtahstu',
                                 password='',
                                 db='test',
                                 port=3306,
                                 charset='utf8')
    sql='select * from spider_index'
    cursor = connection.cursor()
    cursor.execute(sql)
    res=cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    print(res)

if __name__ == "__main__":
    init()