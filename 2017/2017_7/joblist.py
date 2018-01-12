"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@software: PyCharm
@time: 2017/7/22 11:45
"""
import requests

url = "https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false"
header = {}


def getJson(page, kd):
    param = {'first': "false", 'pn': page, 'kd': kd}
    json = requests.post(url, data=param).text
    print(json)


def init():
    getJson('1', 'php')


if __name__ == "__main__":
    init()
