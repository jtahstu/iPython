#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: http://blog.jtahstu.com
# Software: PyCharm
# Time: 2018/5/26 21:11


def init():
    import heapq
    nums = [2, 4, 66, 3, 443, 55, 32, 21, 22, 567, 332, 234, 12, 23]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    portfolio = [
        {'name': 'adas', 'shares': 100, 'price': 62.2},
        {'name': 'adaqs', 'shares': 100, 'price': 312.2},
        {'name': 'adaqs', 'shares': 100, 'price': 12.3},
        {'name': 'adasas', 'shares': 100, 'price': 34.2},
        {'name': 'adaes', 'shares': 100, 'price': 12.2},
        {'name': 'adatgs', 'shares': 100, 'price': 55.2},
    ]
    cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
    print(cheap, expensive)


if __name__ == '__main__':
    init()
