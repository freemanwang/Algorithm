# import random
# class RadomQuickSort(object):
#     def __init__(self):
#         pass
#
#     def swap(self,a,b):
#         a,b = b,a
#     def randIndex(self,start:int, end:int):
#         return random.randint(start, end)
#
#     # def randPart(self, data,leng, start, end):
#     #     if data == None or leng <=0 or start <0 or end >= leng:
#     #         print('Error')
#     #         return None
#     #     index = self.randIndex(start,end)
#     #     # print(index,end)
#     #     self.swap(data[index], data[end])
#     #     small = start - 1
#     #     t = start
#     #     while t < end:
#     #         t+=1
#     #         if data[index] < data[end]:
#     #             small+=1
#     #             if small != index:
#     #                 self.swap(data[index], data[small])
#     #
#     #     small += 1
#     #     self.swap(data[small], data[end])
#     #     return small
#
#     def quickSort(self, data, start, end):
#         i,j = start,end
#         index = self.randIndex(start, end)
#         temp = data[index]
#         while i != j:
#             while data[j] >= temp and i < j:
#                 j-=1
#             while data[i] <= temp and i < j:
#                 i+=1
#             if i < j:
#                 self.swap(data[i], data[j])
#
#         data[i] = temp
#         self.quickSort(data, start, index-1)
#         self.quickSort(data,index+1, end)
#         return
#
#
#

import random
def randomPartiton(lst:list, start:int, end:int):
    index = random.randint(start, end)
    lst[index],lst[end] = lst[end], lst[index]
    return partition(lst, start, end)

def partition(lst:list, start:int, end:int):
    position = start -1
    base = lst[end]
    i = 0
    while i < end:
        i += 1
        if lst[i] <= base:
            position += 1
            lst[position], lst[i] = lst[i], lst[position]

    lst[position+1], lst[end] = lst[end], lst[position+1]
    print(position)
    return position+1

def randomQuickSort(lst:list, start:int, end:int):
    if start < end:
        position = randomPartiton(lst, start, end)
        print(position)
        randomQuickSort(lst, start, position-1)
        randomQuickSort(lst, position+1, end)


def quickSort(lst:list, start:int, end:int):
    if start < end:
        partIndex = partition(lst, start, end)
        quickSort(lst, start, partIndex-1)
        quickSort(lst, partIndex+1, end)
    else:
        return

def partition(lst, start, end):
    watcher = lst[end]
    i = start-1
    j = start
    while j < end-1:
        if lst[j] < watcher:
            i+=1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i+1], lst[end] = lst[end], lst[i+1]
    return i+1

lst = [32,18,22,100,12,65]
# quickSort(lst, 0, len(lst)-1)
# print(lst)

def quick_sort(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)

quickSort(lst,0,len(lst)-1)
print(lst)



