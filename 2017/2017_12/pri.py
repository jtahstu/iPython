"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2017/12/7 16:55
"""


def init():
    noprimes = []
    for i in range(2, 8):
        for j in range(i * 2, 50, i):
            noprimes.append(j)
    print(noprimes)
    primes = []
    for x in range(2, 50):
        if x not in noprimes:
            primes.append(x)
    print(primes)


def listdir():
    import os
    files = [f for f in os.listdir('./') if f.endswith('.py')]
    print(files)


def openx():
    with open('tt.py') as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    # init()
    # listdir()
    openx()
