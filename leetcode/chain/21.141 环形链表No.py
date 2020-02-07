'''
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
'''
from Chain import *

def hasCycle(head:Node, pos:int):
    if head is None:
        return False
    start = head #存储缓开始的位置
    while pos > 0:
        start = start.next
        pos -= 1
    next = head.next
    while next.next is not None and next.next is not start:
        next = next.next
    if next.next == start:
        return True
    return False

# 检测单链表中是否有环，并没告诉第几个节点是环的开始
# 时间复杂度 O(n)，因为会走完所有，而且未必只走一遍
def hasCycle2(head:Node):
    if head is None or head.next is None:
        return False
    fast, slow = head, head.next
    while fast != slow:
        # fast都走到空了还没相遇，那凉了
        if fast is None or fast.next is None:
            return False

        fast = fast.next.next
        slow = slow.next
    # 能走出while循环就是快慢相遇
    return True

# def hasCycle2(head:Node):
