#找出数组里3个数字乘积最大值
def getMax(lst):
    n = len(lst)
    if n < 3:
        return
    if n == 3:
        return lst[0]*lst[1]*lst[2]
    sum = 1
    maxNum = []
    minNum = []
    index = 0
    l1,l2 = lst[:],lst[:]
    for t in range(3):
        tmp = max(l1)
        maxNum.append(tmp)
        l1.remove(tmp)
    for p in range(2):
        tmp = min(l2)
        minNum.append(tmp)
        l2.remove(tmp)
    return max(maxNum[0]*maxNum[1]*maxNum[2],maxNum[0]*minNum[0]*minNum[1])

lst = [1,2,3]
print(getMax(lst))