#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/8/24 11:29

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        import collections
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())

        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        # lookup = collections.defaultdict(int)
        # for i in nums1:
        #     lookup[i] += 1
        #
        # res = []
        # for i in nums2:
        #     if lookup[i] > 0:
        #         res += i,
        #         lookup[i] -= 1
        #
        # return res

def init():
    pass


if __name__ == '__main__':
    init()
