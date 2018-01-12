"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2017/12/7 14:21
"""


def init():
    for i in range(0, 10):
        print(i)
        if i == 11:
            break
    else:
        print("in else")


if __name__ == "__main__":
    print(__name__)
    init()
