
class Fibonacci(object):
    def __init__(self):
        self.result = [0,1]
        pass
    def nthFib(self,n):
        if n < 0:
            return None
        if n < 2:
            return self.result[n]

        fibOne = 1
        fibTwo = 0
        finN = 0
        i = 2
        while i <= n:
            finN = fibOne + fibTwo
            fibTwo = fibOne
            fibOne = finN
            i+=1
        return finN

fib = Fibonacci()
nth = fib.nthFib(100)
print(nth)


