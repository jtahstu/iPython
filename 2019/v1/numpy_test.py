#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Contact: root@jtahstu.com
# Site: i.jtup.cc
# Software: PyCharm
# Time: 2019-03-11 22:11

import numpy as np
from pprint import pprint


def init():
    # print(np.eye(4))

    s = b'Hello World'
    a = np.frombuffer(s, dtype='S1')
    pprint(a)

    x = np.arange(5)
    pprint(x)

    a = [[2, 5], [3, 4]]
    na = np.array(a)
    pprint(na[:, 1])

    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[1, 4], [2, 5], [3, 6]])
    matrix = x.dot(y)  # 矩阵乘法
    pprint(matrix)

    x2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y2 = np.array([[1, 2], [3, 4], [5, 6]])
    pprint(x2.dot(y2))

    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    b = np.array([[5.0, 6.0], [7.0, 8.0]])
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    print("Sum = \n", sum)
    print("Difference = \n", difference)
    print("Product = \n", product)
    print("Quotient = \n", quotient)

    pprint(np.pi)

    # MD Array,
    a = np.array([[11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25],
                  [26, 27, 28, 29, 30],
                  [31, 32, 33, 34, 35]])

    print(a[2, 4])  # >>>25

    # MD slicing
    print(a[0, 1:4])  # >>>[12 13 14]
    print(a[1:4, 0])  # >>>[16 21 26]
    print(a[::2, ::2])  # >>>[[11 13 15]
    #     [21 23 25]
    #     [31 33 35]]
    print(a[:, 1])  # >>>[12 17 22 27 32]

    print(type(a))  # >>><class 'numpy.ndarray'>
    print(a.dtype)  # >>>int32
    print(a.size)  # >>>25
    print(a.shape)  # >>>(5, 5)
    print(a.itemsize)  # >>>8
    print(a.ndim)  # >>>2
    print(a.nbytes)  # >>>200


def basic():
    # Basic Operators
    a = np.arange(25)
    a = a.reshape((5, 5))

    b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
                  4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
                  56, 3, 56, 44, 78])
    b = b.reshape((5, 5))

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a ** 2)
    print(a < b)
    print(a > b)

    print(a.dot(b))


def bool_mask():
    # Boolean masking
    import matplotlib.pyplot as plt

    a = np.linspace(0, 2 * np.pi, 50)
    b = np.sin(a)
    plt.plot(a, b)
    mask = b >= 0
    plt.plot(a[mask], b[mask], 'bo')
    mask = (b >= 0) & (a <= np.pi / 2)
    plt.plot(a[mask], b[mask], 'go')
    plt.show()


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


if __name__ == '__main__':
    # init()
    # basic()
    # bool_mask()
    print(quicksort([3, 6, 8, 10, 1, 2, 1]))

    pprint(np.random.random((5,5)))
