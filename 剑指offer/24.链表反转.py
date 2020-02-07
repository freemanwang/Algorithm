from SingleChain import *
def reverseChain(head:Node):
    '''
    将链表反转
    :param head:链表的头节点（头节点的下一节点才是存数据的有效节点）
    :return: 反转后链表的节点
    '''
    # 下面3种判别分别是：是否节点、空指针、仅1个空头、链表长为1
    if not isinstance(head,Node) or not head or head.next == None or not head.next.next:
        return
    rtn = head
    pre = None
    node = head.next
    next = None
    # 当前节点后面还有节点时：
    while node.next:
        next = node.next
        node.next = pre
        pre = node
        node = next
    #  最后一个节点，将其指向倒数第一个
    node.next = pre
    # head指向最末尾节点，反转已完成
    head.next = node

lst = [1,2,3,4,5]
chain = SingleChain()
chain = chain.createChain(lst)
# reverseChain([])
chain.reverseChain()
chain.printChain()
