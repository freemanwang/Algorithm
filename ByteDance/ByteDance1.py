#给一个数组，生成一个链
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    def hasNext(self):
        if self.next:
            #print('has next')
            return True
       # print('end')
        return False
class Chain:
    def __init__(self):
        self.head = Node()
        self.head.data = 'I\'m head of this chain'
        self.capacity = 0

    def arr2Chain(self,arr:list):
        if not arr:
            return
        # length = len(arr)
        count = 0
        index = self.head
        for t in arr:
            tmpNode = Node(t)
            index.next = tmpNode
            index = tmpNode
            count +=1
        self.capacity = count
        return self

    def printChain(self):
        if self.capacity == 0:
            return
        node = self.head.next
        while node:
            if node.hasNext():
                print(node.data ,end='=>')
                node = node.next
            else:
                print(node.data)
                node = None

arr = [10,20,30,40,50]
chain = Chain()
chain = chain.arr2Chain(arr)
chain.printChain()