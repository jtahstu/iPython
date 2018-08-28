#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/8/24 10:16

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = {}
    for k, v in enumerate(nums):
        if v in res:
            res[v] += 1
        else:
            res[v] = 1
    for (k, v) in res.items():
        if v == 1:
            return k

    # return sum(list(set(nums))) * 2 - sum(nums)

    # n = 0
    # for num in nums:
    #     n ^= num
    # return n

def init():
    l = [4, 1, 2, 1, 2]
    print(singleNumber(l))


if __name__ == '__main__':
    init()
