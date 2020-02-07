class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleChain():
    def __init__(self):
        '构造方法，生成一个带头尾指针的空单链表'
        self.head = Node("I am the head node")
        self.tail = self.head
        return

    def addInhead(self, data):
        '在头部加入节点'
        node = Node(data)
        if self.head == None:  # 空队列则+的节点为头节点
            self.head = node
            self.tail = node
        else:  # 链表头节点改成+的节点，让它指向原本头节点
            node.next = self.head
            self.head = node

    def addInTail(self, data):
        '在尾部加入节点'
        node = Node(data)
        if self.tail == None:  # 队列为空
            self.head = node
            self.tail = node
        else:  # 加在末尾，尾指针指向新加节点
            self.tail.next = node
            self.tail = node

    def delNodeByData(self, data):
        '参数为要删的节点的数据，功能为删除该节点'
        if self.head != None:
            stnode = self.head
            if stnode.data == data:  # 要删的是头节点
                if self.head.next != None:
                    self.head = self.head.next
                    del stnode
                    print(f'删除数据为{data}节点成功')
                    return True
        else:
            print('空链！')
            return False
        while stnode.next != None:  # 从头节点下一个开始检查
            if stnode.next.data == data:
                if stnode.next.next != None:  # 删除链中头尾之间的节点
                    tmp = stnode.next
                    stnode.next = stnode.next.next
                    del tmp
                    print(f'删除数据为{data}节点成功')
                    return True
                else:  # 要删的节点是最后一个节点
                    del stnode.next
                    stnode.next = None
                    self.tail = stnode  # 尾指针指向新的最后
                    print(f'删除数据为{data}节点成功')
                    return True
            else:
                stnode = stnode.next
        print(f'无数据为{data}的节点，删除失败')
        return False

    def getLength(self):
        '求单链长度，返回int'
        leng = 0
        if self.head != None:
            index = self.head
            leng += 1
        else:
            return 0
        while index.next != None:
            leng += 1
            index = index.next
        return leng

    def printChain(self):
        '打印单链表'
        if self.head == None:
            print('空链表')
            return
        elif self.head and not self.head.next:
            start = self.head
            print(f'仅有一个头节点，没有实际数据节点。')
        else:

            print(f'|headNode|data:{self.head.data}|next-->')
            start = self.head.next
        while start:
            if start.next:
                print(f'|data:{start.data}|next-->')
            else:
                print(f'|data:{start.data}')
            start = start.next  # 这样操作，到链表最后一个时，会因为没有下一个所以不打印下一个，就不报错。
        # print(f'None')
        print('打印完毕')
        return True

    def createChain(self, lst):
        '从list或tuple中读取数据生成单链'
        if not lst and (isinstance(lst, list) or isinstance(lst, tuple)):
            print('序列非法')
            return False
        if len(lst) <= 0:
            print('空序列')
            return False

        start = self.head
        for t in lst:
            node = Node(data=t)
            start.next = node
            start = start.next
        self.tail = start
        print('创建完成')
        # self.printChain()
        return self

    def getKthNode(self,k):
        if not self.head or k <=0:
            return
        p1 = self.head.next
        #使p1指向第1个节点，p2指向第k-1个节点。p1和p2之间间隔k-1个节点
        # 如果p1还没走到第k个节点就没有后续了，那链表长度不足，不可能有第k个节点，return False
        t = 1
        while t in range(k - 1):
            if p1.next:
                t += 1
                p1 = p1.next
            else:
                return False
        #p1,p2同时向后遍历，当p2指向倒数第1节点时，p1指向的就是倒数第（1+k-1）个节点
        return p1


    def getLastKthNode(self,k):
        if not self.head or k <=0:
            return
        p1 = self.head.next
        p2 = self.head.next
        #使p1指向第1个节点，p2指向第k-1个节点。p1和p2之间间隔k-1个节点
        # 如果p2还没走到第k-1个节点就没有后续了，那链表长度不足，不可能有倒数第k个节点，return False
        t = 0
        while t in range(k - 1):
            if p2.next:
                t += 1
                p2 = p2.next
            else:
                return False
        #p1,p2同时向后遍历，当p2指向倒数第1节点时，p1指向的就是倒数第（1+k-1）个节点
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        # print(p2.data,p1.data)
        return p1

    def reverseChain(self):
        '''
        将链表反转
        :param head:链表的头节点（头节点的下一节点才是存数据的有效节点）
        :return: 反转后链表的节点
        '''
        head = self.head
        # 下面3种判别分别是：是否节点、空指针、仅1个空头、链表长为1
        if not isinstance(head, Node) or not head or head.next == None or not head.next.next:
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

def decoration(old):
    def new_func(*args, **kwargs):
        print('开始打印')
        old(*args, **kwargs)
        print('打印完毕')
    return new_func()





# lst = [1,2,3,4,5,6]
# chain = SingleLinkedList()
# chain = chain.createChain(lst)
# p1 = chain.getLastKthNode(8)
# p2 = chain.getKthNode(7)
# print('倒数第3个节点数据是：',p1.data)
# print('第3个节点数据是：',p2.data)

# lst = [1, 2, 3, 4, 5]
# chain = SingleLinkedList()  # 从list建chain成功
# chain.createChain(lst)
# chain.addInhead(10)  # 头+成功
# chain.printList()
# chain.addInTail(100)  # 尾+成功
# chain.printList()
# chain.delNodeByData(10)
# chain.printList()  # 删头成功
# chain.delNodeByData(100)
# chain.printList()  # 尾删成功
# chain.delNodeByData(3)
# chain.printList()  # 中间删成功
# print(chain.getLength())  # 求长成功
#
# nullList = []
# nullListBuildChain = SingleLinkedList()
# nullListBuildChain.createChain(nullList)


