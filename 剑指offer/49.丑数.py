# 把只包含质因子2，3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但7、14不是，因为它们包含质因子7。 习惯上我们把1当做是第一个丑数。
#判断一个数是不是丑数直接除就行，但如果需要求第几个丑数，存下前面已经算过的丑数或许更好。因为能避免很多计算

# 下面是求 第n个丑数 的方法
def getUglyNum(n:int):
    ug2, ug3, ug5 = 1, 1, 1
    lst = [1]
    count = 1 #第几个丑数，1是第一个
    while count <= n:
        curUgly = min(ug2*2, ug3*3, ug5*5)
        if curUgly == ug2 * 2:
            ug2 *= 2
        if curUgly == ug3 * 3:
            ug3 *= 3
        if curUgly == ug5 * 5:
            ug5 *= 5
        count += 1
        lst.append(count)
    return lst[n-1]

def isUglyNum(num:int):
    while num % 2 == 0:
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 5
    return num == 1

n = 1500
print(isUglyNum(n))

