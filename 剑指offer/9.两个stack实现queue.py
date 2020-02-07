from Stack import *
import copy
class QueueMadeBy2Stacks(object):
    def __init__(self,len):
        self.capcity = len
        self.s1 = Stack(len)
        self.s2 = Stack(len)

    def inS(self, s:Stack, data):
        if s.empty > 0:
            s.push(data)
        else:
            print('栈满')
            return False

    def outS(self, s1:Stack, s2:Stack):
        t = s1.pop()
        lst = []
        while s1.used > 0:
            tmp = s1.pop()
            lst.insert(0,tmp)
        #print(lst)
        for tmp in lst:
            s2.push(tmp)
        return t

    def inQueue(self,data):
        if self.s1.empty > 0 and self.s2.used== 0:
            self.inS(self.s1, data)
        elif self.s2.empty > 0 and self.s1.used == 0:
            self.inS(self.s2, data)
        else:
            print(f'队已满，{data}入队失败')
            return

    def outQueue(self):
        if self.s1.used > 0:
            return self.outS(self.s1, self.s2)
        elif self.s2.used > 0:
            return self.outS(self.s2, self.s1)
        else:
            print('队为空')
            return

    def printQueue(self):
        if self.s1.used > 0:
            self.s1.printStack()
        elif self.s2.used > 0:
            self.s2.printStack()
        else:
            print('队为空')

que = QueueMadeBy2Stacks(10)
que.inQueue(1)
que.inQueue(2)
que.inQueue(3)
que.inQueue(4)
que.inQueue(5)
que.inQueue(6)
que.inQueue(7)
que.inQueue(8)
que.inQueue(9)
que.inQueue(10)
que.inQueue(111)
que.printQueue()
#que.s1.printStack()
#que.s2.printStack()
#que.printQueue()

print(que.outQueue())
que.printQueue()
# que.s1.printStack()
# que.s2.printStack()
