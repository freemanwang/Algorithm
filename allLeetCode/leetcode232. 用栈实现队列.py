'''
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
在真实的面试中遇
'''


class MyQueue(object):

    def __init__(self, capacity=10):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.used = 0
        self.emp = capacity
        self.instack = []
        self.outstack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if self.emp > 0:
            self.instack.append(x)
            self.emp -= 1
            self.used += 1
            return True
        else:
            print('队列已满')
            return False

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.used > 0:
            if len(self.outstack) > 0:
                self.used -= 1
                return self.outstack.pop()
            else:
                while len(self.instack) > 0:
                    self.outstack.append(self.instack.pop())
                return self.pop()
        else:
            print('队列空，无法pop')

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.used > 0:
            tmp = self.pop()
            self.outstack.append(tmp)
            self.used += 1
            self.emp -= 1
        else:
            print('队列为空,无法peek')
            return False


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.used > 0:
            return False
        return True
# Your MyQueue object will be instantiated and called as such:

obj = MyQueue()
x = 3
obj.push(x)
obj.push(5)
obj.push(7)
param_2 = obj.pop()
# print(obj.instack)
# print(obj.outstack)
print(param_2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)
