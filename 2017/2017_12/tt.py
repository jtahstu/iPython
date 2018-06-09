"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2017/12/6 18:29
"""


def e(n):
    if n > 0:
        n -= 1
        e(n)
        print(n)
        n -= 1
        e(n)

a = 3
e(a)

