"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
"""
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
def createChainWithoutHead(lst):
    '''
    从list或tuple中读取数据生成单链
    :param lst:
    :return: 链表头节点，头节点的下一个节点才开始放数据
    '''

    if not lst and (isinstance(lst, list) or isinstance(lst, tuple)):
        print('序列非法')
        return False
    if len(lst) <= 0:
        print('空序列')
        return False
    head = Node(lst[0])
    start = head
    for t in lst[1:]:
        node = Node(val=t)
        start.next = node
        start = start.next
    print('创建完成')
    return head

def printChain(node):
    '''
    打印单链表
    :param node:链表第一个数据节点
    :return: 打印成功True,其他False
    '''

    if not node:
        print('输入为空')
        return False
    start = node
    while start:
        if start.next:
            print(f'|data:{start.val}|next-->')
        else:
            print(f'|data:{start.val}')
        start = start.next  # 这样操作，到链表最后一个时，会因为没有下一个所以不打印下一个，就不报错。
    # print(f'None')
    print('打印完毕')
    return True

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        主要是使用归并的思路 先分再合
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        return self.minute(head)

    def minute(self, head):
        """
        这个方法主要是实现分的操作
        分的过程用快慢指针实现
        :param head:
        :return:
        """
        if head.next is None:
            return head
        quick, slow, temp = head, head, head
        while quick is not None and quick.next is not None:
            temp = slow
            slow = slow.next
            quick = quick.next.next
        temp.next = None  # 这一步就是将整个链表从中间分开 失去这一步 后面将无限循环

        i = self.minute(head)
        j = self.minute(slow)
        return self.Combined(i, j)

    def Combined(self, i, j):
        """
        这个方法主要实现合的操作
        合的过程就是从i 和 j开始比较 就是从开头和中间开始比较 将两个相比小的排在head后
        最后返回head即可
        :param i:ListNode
        :param j:ListNode
        :return:
        """
        TempNode = ListNode(0)
        temp = TempNode
        while i is not None and j is not None:
            if i.val <= j.val:
                temp.next = i
                i = i.next
            else:
                temp.next = j
                j = j.next
            temp = temp.next
        if i is not None:
            temp.next = i
        if j is not None:
            temp.next = j
        return TempNode.next


if __name__ == '__main__':
    node = ListNode(4)
    node.next = ListNode(2)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(3)
    print(Solution().sortList(node))

lst = [4,2,1,3]
head = createChainWithoutHead(lst)
c = Solution()
lst = c.sortList(head)
printChain(lst)
