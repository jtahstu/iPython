#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/8/23 15:49

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if len(prices) < 2:
        #     return 0
        # i = 0
        # sum = 0
        # for j in range(1, len(prices)):
        #     if prices[j] < prices[j - 1]:
        #         sum = sum + prices[j - 1] - prices[i]
        #         i = j
        #     if j == len(prices) - 1 and i != j:
        #         sum = sum + prices[j] - prices[i]
        #
        # print(sum)
        # return sum
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        print(ans)
        return ans


def init():
    l = [7, 1, 5, 3, 6, 4]
    l2 = [7, 6, 4, 3, 1]
    l3 = [1, 2, 3, 4, 5,4,3,2,1,2]
    Solution().maxProfit(l3)


if __name__ == '__main__':
    init()
