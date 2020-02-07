class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def createChain(lst):
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
    head = Node('头节点')
    start = head
    for t in lst:
        node = Node(data=t)
        start.next = node
        start = start.next
    print('创建完成')
    return head

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
        node = Node(data=t)
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
            print(f'|data:{start.data}|next-->')
        else:
            print(f'|data:{start.data}')
        start = start.next  # 这样操作，到链表最后一个时，会因为没有下一个所以不打印下一个，就不报错。
    # print(f'None')
    print('打印完毕')
    return True


def mergeChain(node1,node2):
    '''
    按大小合并2个链，较小者在前
    :param node1: 链1的第一个数据节点
    :param node2: 链2的第一个数据节点
    :return: 合并链的第一个数据节点
    '''
    # node1,node2只要不是全非空，就返回。因为哪怕就1个空，都没什么好合并的
    if not node1:
        return node2
    if not node2:
        return node1
    # 任何一个不是节点，退出
    if not isinstance(node1, Node) or not isinstance(node2, Node):
        return
    if node1.data <= node2.data:
        mergeHead = node1
        mergeHead.next = mergeChain(node1.next, node2)
    else:
        mergeHead = node2
        mergeHead.next = mergeChain(node1, node2.next)
    print('合并完成')
    return mergeHead