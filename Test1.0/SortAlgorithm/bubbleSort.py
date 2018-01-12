# 冒泡排序
# 它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
def BubbleSort(lists):
    for i in range(0,len(lists)):
        for j in range(i+1,len(lists)):
            if lists[i]>lists[j]:
                lists[i],lists[j]=lists[j],lists[i]
    return lists

list = [5, 4, 7, 8, 9, 1, 2, 3, 6]
BubbleSort(list)
print(list)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
BubbleSort(list2)
print(list2)

list3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
BubbleSort(list3)
print(list3)