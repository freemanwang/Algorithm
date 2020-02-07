'''
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:
你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 isempty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
在真实的面试
'''

import queue

class MyStack(object):

    def __init__(self,capacity:int=20):
        self.queA = []
        self.queB = []
        self.used = 0
        self.emp = 20
        self.capacity = capacity

    def push(self, x):
        if self.emp > 0:
            self.queA.append(x)
            self.used += 1
            self.emp -= 1
            return True
        else:
            print('栈已满')
            return False

    def pop(self):
        if self.used > 0:
            while len(self.queA) > 1:
                self.queB.put_nowait(self.queA.pop(0))
            tmp = self.queA.pop()
            self.queA, self.queB = self.queB, []
            self.used -= 1
            self.emp += 1
            return tmp
        else:
            print('栈空，无法pop')
            return False

    def top(self):
        if self.used > 0:
            tmp = self.pop()
            self.push(tmp)
            return tmp
        else:
            print('栈空，无法pop')
            return False

    def empty(self):
        if self.used > 0:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
param_4 = obj.empty()

# qa = queue.Queue(5)
# for t in range(5):
#     qa.put_nowait(t)
# qb =qa
# print(qa.get())
# print(qa.get())
# print(qb.get())
# print(qa.get())
