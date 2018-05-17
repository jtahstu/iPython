"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/5/15 16:21
"""

from pprint import pprint


def init():
    with open("./data/ifb.bwe.io.access_log-20180512", "r") as r:
        lines = r.readlines()
    pprint(lines[0:5])
    for line in lines[0:10]:
        [ips, infos] = line.split('- -')
        pprint(ips)


if __name__ == "__main__":
    init()
