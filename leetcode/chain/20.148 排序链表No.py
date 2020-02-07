'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
'''
from Chain  import *
class Solution:
    def sortChain(self, head):
        if not head:
            return
        if head.next is None:
            return head
        return self.partInMiddle(head)

    def partInMiddle(self, head):
        if head.next is None: #如果长度只有1，就不继续切分了，返回去和另一个长1的合并成长2且有序的链表
            return head
        quick, slow, tmp = head, head, head
        while quick is not None and quick.next is not  None:
            tmp = slow  #跟着慢走，而且是上一次的慢，
            # 因为如果本次quick到尾了，那么slow就是中间，上次slow就是中间的前一个
            slow = slow.next  #慢一次前进一个
            quick = quick.next.next  #快一次前进2个
        tmp.next = None  #把前半部分和后半部分割裂开
        front = self.partInMiddle(head) #前半部分递归2分
        back = self.partInMiddle(slow) #后半部分递归2分
        return self.combine(front, back)

    def combine(self, front, back):
        #合并后的链应有序，因从长为1的2个链递归合上来，所以拿来合并的链自身有序
        tmpNode = Node()
        current = tmpNode
        while front is not None and back is not None:
            if front.data <= back.data:
                current.next = front
                front = front.next
            else:
                current.next = back
                back = back.next
            current = current.next

        if front is not None:
            current.next = front
        if back is not None:
            current.next = back
        return tmpNode.next

# def partiton(start:Node, end:Node):
#     data = start.data
#     p, q = start, start.next
#     while q != end:
#         # 如果后面的小于基准元素，把它换到前面来。
#         # 如果当前元素小于data，q 和 p.next 指向同一个，交换实际上没什么用
#         # 但若有 >data 的元素，则单纯的 q 后移， p 不会后移，即p的下一个元素是比data大的，
#         # 这样 q 找到一个比 data 小的元素时，和p.next交换的意义就很明确了
#         if q.data < data:
#             p = p.next
#             swap(p, q)
#         q = q.next
#     # 让基准元素到中间
#     swap(start, p)
#     # 返回基准节点
#     return p
#
# def sortChain(start:Node, end:Node):
#     if start != end:
#         pivot = partiton(start, end)
#         sortChain(start, pivot)
#         sortChain(pivot.next, end)
#
# def swap(p:Node, q:Node):
#     '''
#     交换2节点值
#     '''
#     p.data, q.data = q.data, p.data

# 链表快排
lst = [4,2,1,3]
head = createChainWithoutHead(lst)
printChain(head)
c = Solution()
c.sortChain(head)
printChain(head)
# printChain(head)



