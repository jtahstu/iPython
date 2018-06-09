"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: quickSort.py
@time: 2017/01/05 22:22
"""
# 快速排序
# 描述
#
# 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
def quickSort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quickSort(lists, low, left - 1)
    quickSort(lists, left + 1, high)
    return lists


list = [5, 4, 7, 8, 9, 1, 2, 3, 6]
quickSort(list,0,8)
print(list)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quickSort(list2,0,8)
print(list2)

list3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
quickSort(list3,0,8)
print(list3)