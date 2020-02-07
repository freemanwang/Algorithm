def maxCuttingSolution(length:int):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    #多剪长为3的段
    timeOf3 = length // 3

    #当最后剩下长度为4时减2*2，比3*1好
    if length - timeOf3*3 == 1:
        timeOf3 -= 1
    timeOf2 = (length - timeOf3*3) // 2
    print('长为3的段有：',timeOf3,'段；        ','长为2的段有：',timeOf2,'段')
    return pow(3,timeOf3) * pow(2,timeOf2)

max = maxCuttingSolution(7)
print(max)