"""
@author: jtusta
@license: MIT Licence 
@contact: root@jtahstu.com
@site: www.jtahstu.com
@software: PyCharm Community Edition
@file: selectSort.py
@time: 2017/01/07 13:19
"""
# 直接选择排序
# 描述
#
# 基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
def selectSort(lists):
    for i in range(0, len(lists)):
        min = i
        for j in range(i + 1, len(lists)):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


list = [5, 4, 7, 8, 9, 1, 2, 3, 6]
selectSort(list)
print(list)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
selectSort(list2)
print(list2)

list3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
selectSort(list3)
print(list3)
