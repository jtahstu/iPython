"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2017/12/7 14:43
"""


def init():
    '''
    Python 推导式
    by jtahstu
    '''
    list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
    l_count = {c: list.count(c) for c in list}
    print(l_count)


if __name__ == "__main__":
    init()
    help(init)
