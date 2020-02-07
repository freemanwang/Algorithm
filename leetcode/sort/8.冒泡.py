# 把大的冒泡到后面
def bubleSort(lst:list):
    if not lst:
        return
    # 不改变传入数组
    lst = lst[:]
    length = len(lst)
    i = length -1
    # 比的范围每次-1，因为每次总有1个当前最大挪到后面
    while i > 0:
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        i -= 1
    return lst

lst = [2,63,22,5,9,32,54,8,13,32]
l = bubleSort(lst)
print(lst)
print(l)
