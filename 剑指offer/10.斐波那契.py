#本方法适合各种上楼梯跳台阶啥的
def getFibNth(n:int):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    fib1 = 1
    fib2 = 0
    for i in range(2,n+1):
        fibn = fib1 + fib2
        fib2 = fib1
        fib1 = fibn

    return fibn

print(getFibNth(100))