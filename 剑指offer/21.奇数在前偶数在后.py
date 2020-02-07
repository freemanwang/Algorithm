def isOdd(num:int):
    return num % 2
def isEven(num:int):
    return not (num % 2)

def sorLst(lst:list):
    if not lst or len(lst)==0:
        return
    pre = 0
    end = len(lst)-1
    while(end > pre):
        while pre < end and isOdd(lst[pre]):
            pre += 1
        while pre < end and isEven(lst[end]):
            end -= 1

        if pre < end and isEven(lst[pre]) and isOdd(lst[end]):
            lst[pre],lst[end] = lst[end],lst[pre]
lst = [1,2,3,4,5]
sorLst(lst)
print(lst)


# 某种判别机制,这里设置成，是否为负数。那么函数就会是，负数在前，非负数在后
def func(num):
    return  num < 0

# 更具普适性的方法，可以针对多种划分，比如正负分，能不能被3整除等待，根据传参进去的判别函数决定
def sortByFunc(lst:list):
    if not lst or len(lst) == 0:
        return
    pre = 0
    end = len(lst)-1
    while end > pre:
        while pre<end and func(lst[pre]):
            pre += 1
        while pre<end and not func(lst[end]):
            end -= 1
        if pre < end:
            lst[pre], lst[end] = lst[end], lst[pre]

lst2 = [3,6,-8,0,43,-99,32,-30,6]
sortByFunc(lst2)
print(lst2)

