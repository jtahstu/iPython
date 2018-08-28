#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/8/23 15:27

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(sorted(set(nums)))
        del nums[len(s):]
        for i in range(len(s)):
            nums[i] = s[i]
        print(nums)
        return len(nums)


def init():
    l = [-1,0,0,0,0,3,3]
    Solution().removeDuplicates(l)


if __name__ == '__main__':
    init()