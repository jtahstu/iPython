#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/8/23 18:09

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tmp = nums[:]
        length = len(nums)
        for i in range(0, k):
            nums[i] = tmp[length - k + i]
        for j in range(k, length):
            nums[j] = tmp[j - k]
        return nums

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


def init():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 8 % 7
    print(Solution().rotate(nums, k))


if __name__ == '__main__':
    init()
