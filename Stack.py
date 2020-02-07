class Stack(object):
    '''
        创建一个容量为len的Stack
    '''
    def __init__(self,len):
        self.stack = []
        self.capcity = len
        self.empty = len
        self.used = 0
    def push(self,data):
        if self.empty > 0:
            self.stack.append(data)
            self.empty -= 1
            self.used += 1
            return True
        else:
            print('The stack is full!')
            return False
    def pop(self):
        if self.capcity - self.empty > 0:
            self.empty += 1
            self.used -= 1
            return self.stack.pop()
    def getEnmty(self):
        return self.empty
    def getUsed(self):
        return self.used
    def getStackSize(self):
        return self.capcity
    def printStack(self):
        if self.used > 0:
            for t in self.stack[-1:-len(self.stack)-1:-1]:
                print(f'|%10s|'%str(t).center(10))
            print('-'*12)


# stk = Stack(10)
# stk.push(1)
# stk.push(2)
# stk.push(3)
# stk.push(4)
# stk.push(5)
# stk.printStack()  #OK的
# print(stk.pop())
# stk.printStack()
