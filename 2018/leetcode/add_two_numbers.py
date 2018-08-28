#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: blog.jtahstu.com
# Software: PyCharm
# Time: 2018/8/23 10:29

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

from pprint import pprint


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, val):
        item = ListNode(val)

        node = self
        while node.next:
            node = node.next
        node.next = item

    def __repr__(self):
        node = self
        list = [self.val]
        while node.next:
            node = node.next
            list.append(node.val)
        return str(list)


class Solution:
    def addTwoNumbers0(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_node = ListNode(0)
        list_node.append(3)
        list_node.append(2)
        list_node.append(1)
        print(list_node)

    def addTwoNumbers(self, l1, l2):
        head = ListNode((l1.val + l2.val) % 10)
        current = head
        carry = (l1.val + l2.val) // 10
        while l1.next is not None or l2.next is not None:
            num1 = 0
            num2 = 0
            if l1.next is not None:
                l1 = l1.next
                num1 = l1.val
            if l2.next is not None:
                l2 = l2.next
                num2 = l2.val
            current.next = ListNode((num1 + num2 + carry) % 10)
            carry = (num1 + num2 + carry) // 10
            current = current.next
        if carry != 0:
            current.next = ListNode(carry)
        return head


def init():
    s = Solution()
    s.addTwoNumbers0()


if __name__ == '__main__':
    init()
