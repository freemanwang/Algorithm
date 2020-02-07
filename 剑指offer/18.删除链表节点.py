#
# coding=utf-8
import sys


class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next


class Chain:
    def __init__(self):
        head = Node()
        self.head = head

    def createChain(self, lst: list):
        index = self.head
        for t in lst:
            tmpNode = Node(t)
            index.next = tmpNode
            index = index.next

    def printChain(self):
        index = self.head
        while index.next:
            index =index.next
            print(index.data)

    def delNode(self,node: Node):
        tmp = node
        if node.next:
            node.data = node.next.data
            node.next = node.next.next
        del tmp


lst = [5, 10, 15, 20]
chain = Chain()
chain.createChain(lst)
chain.printChain()
print(chain.head)
chain.delNode(chain.head.next.next)
chain.printChain()