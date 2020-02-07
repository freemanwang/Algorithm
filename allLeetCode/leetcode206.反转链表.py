# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Chain import *

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if head.next == None:
            return head

        stack = []
        while head is not None:
            stack.append(head)
            head = head.next

        resHead = stack.pop()
        index = resHead
        while len(stack) > 0:
            index.next = stack.pop()
            index = index.next
        # 把最后一个节点的 next 清空
        index.next = None
        return resHead

    def reverseList2(self, head):
        cur, prev = head, None
        while cur:
            # 注意，别被固有印象带歪了，cur.next = pre(意思是cur.next=None)并不会影响后面的赋值，也就是说执行完前面那个指令，最后面的 cur = cur.next != None,python会在执行前先把右侧的值存好，否则结构化赋值就没意义了
            cur.next, prev, cur = prev, cur, cur.next
        return prev

lst = [1,2,3,4]
c= Solution()
head = createChainWithoutHead(lst)
printChain(head)
res = c.reverseList2(head)
printChain(res)