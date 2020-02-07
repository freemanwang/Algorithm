'''
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：
MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

示例：
MyCircularQueue circularQueue = new MycircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4

提示：
所有的值都在 0 至 1000 的范围内；
操作数将在 1 至 1000 的范围内；
请不要使用内置的队列库。
'''


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.data = [None]*self.capacity
        self.front = 0
        self.tail = 0
        self.empty = k
        self.used = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.empty > 0:
            self.data[self.tail] = value
            self.tail = (self.tail + 1)%self.capacity
            self.empty -= 1
            self.used += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.used > 0:
            self.data.pop(self.front)
            self.data.insert(self.front,None)
            self.front = (self.front + 1) % self.capacity
            self.empty += 1
            self.used -= 1
            return True
        else:
            return False


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.used > 0:
            return self.data[self.front]
        else:
            return -1


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.used > 0:
            return self.data[(self.tail-1)%self.capacity]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.used > 0:
            return False
        return True

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.empty > 0:
            print(self.empty)
            return False
        return True


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_1 = obj.enQueue(3)
# param_1 = obj.enQueue(4)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
print(obj.isFull(),1111111)
print(obj.data)
print(obj.deQueue())
print(obj.data)
print(obj.Front())
print(obj.Rear())
print(obj.Rear())
print(obj.Rear())
print(obj.Rear())
print(obj.data)
print(obj.isEmpty())

