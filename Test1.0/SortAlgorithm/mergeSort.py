"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: mergeSort.py
@time: 2017/01/07 14:51
"""


# 归并排序
#
# 描述
#
# 归并排序是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。
#
# 归并过程为：比较a[i]和a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到r[k]中，并令i和k分别加上1；否则将第二个有序表中的元素a[j]复制到r[k]中，并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]。

def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


def mergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = mergeSort(lists[:num])
    right = mergeSort(lists[num:])
    return merge(left, right)


list = [5, 4, 7, 8, 9, 1, 2, 3, 6]
listx = mergeSort(list)
print(listx)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listy = mergeSort(list2)
print(listy)

list3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
listz= mergeSort(list3)
print(listz)
