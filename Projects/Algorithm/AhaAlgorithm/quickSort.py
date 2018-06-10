"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: quickSort.py
@time: 2017/01/10 18:25
"""

list = [5, 4, 7, 8, 9, 1, 2, 3]
print(list)


def quickSort(left, right):
    if left > right:
        return
    temp = list[left]
    i = left
    j = right
    while (i != j):
        while list[j] >= temp and i < j:
            j -= 1
        while list[i] <= temp and i < j:
            i += 1
        if i < j:
            list[i], list[j] = list[j], list[i]
    list[left] = list[i]
    list[i] = temp

    quickSort(left, i - 1)
    quickSort(i + 1, right)


quickSort(0, len(list) - 1)
print(list)
