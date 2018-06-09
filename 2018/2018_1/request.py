"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/1/22 10:59
"""
from pprint import pprint

import requests


def init():
    r = requests.get('http://i.jtup.cc')
    print(r)


if __name__ == "__main__":
    init()
