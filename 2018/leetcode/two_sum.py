#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/8/22 18:28

from pprint import pprint


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # s_nums = list(sorted(nums))
    # r_nums = list(reversed(s_nums))
    # find_x = 0
    # find_y = 0
    # for i in s_nums:
    #     for j in r_nums:
    #         if i + j < target:
    #             break
    #         if i + j == target:
    #             find_x = i
    #             find_y = j
    # index_x = -1
    # index_y = -1
    # for k, v in enumerate(nums):
    #     if v == find_x and index_x == -1:
    #         index_x = k
    #     if v == find_y and index_x != k:
    #         index_y = k
    #     if index_x != -1 and index_y != -1:
    #         break
    # return [index_x, index_y]

    hash = {}
    for k, v in enumerate(nums):
        if v not in hash.keys():
            hash[v] = k
        if (target - v) in hash.keys() and  hash[target - v] != k:
            return [hash[target - v], k]

    # dict = {}
    # for i, value in enumerate(nums):
    #     another = target - value
    #     if another in dict.keys():
    #         j = dict[another]
    #         return [j, i]
    #     else:
    #         dict[value] = i

    # if len(nums) <= 1:
    #     return False
    #
    # buff_dict = {}
    # for i in range(len(nums)):
    #     if (target - nums[i]) in buff_dict:
    #         print(buff_dict)
    #         return [buff_dict[target - nums[i]], i]
    #     else:
    #         buff_dict[nums[i]] = i


def init():
    print(twoSum([2,3,4,10,7,11,15], 9))


if __name__ == '__main__':
    init()
