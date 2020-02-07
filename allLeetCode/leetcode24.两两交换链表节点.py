from Chain import *

# 偶数个节点就完全交换，奇数的话最后落单的不换
def swapPairs(head):
    res = Node('tmp')
    res.next = head
    front = res # 指向转换完链的最后一个

    while front.next is not None and front.next.next is not None:
        first = front.next
        second = front.next.next

        # 交换 2 节点
        # first.next = second.next
        # second.next = front.next
        first.next, second.next = second.next, front.next

        # 把 从后转前的那个节点 连接到前面的链
        front.next = second

        # front 指向已转换链最后一个节点
        front = first

    return res.next

def swapPairsRecurse(head):
    pass

lst = [1,2,3,4]
c = createChainWithoutHead(lst)
printChain(c)
res = swapPairs(c)
printChain(res)