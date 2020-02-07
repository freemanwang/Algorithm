# 选小的放前面

def selectSort(lst:list):
    if not lst:
        return
    lst = lst[:]
    length = len(lst)
    index = 0
    # 倒数第二个和最后一个比一下，谁小谁在前，不用走到最后一个去比，所以 截止到 length-1-1
    while index < length-1:
        min = lst[index]
        minIndex = index
        for i in range(index+1, length):
            if lst[i] < min:
                min = lst[i]
                minIndex = i
        # 起始处元素不是最小的，那么和最小元素交换
        if minIndex != index:
            lst[minIndex], lst[index] = lst[index], lst[minIndex]
        # 本次选择排序结束，从下一个元素开始继续选择排序
        index += 1
    # 排序完成
    return lst

lst = [2,63,22,5,9,32,54,8,13,32]
l = selectSort(lst)
print(lst)
print(l)