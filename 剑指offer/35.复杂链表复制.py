# 复杂链表的复制
class ComplexNode:
    def __init__(self, val=None, next=None, sibling=None):
        self.val = val
        self.next = next
        self.sibling = sibling

def creatComplexChain():
    '''
    自定义的生成一个如书上示例的复杂链，写死的方法
    :return: Node_A
    '''
    valList = ['A', 'B', 'C', 'D', 'E']
    head = ComplexNode(val=valList[0])
    index = head
    # nodes = {}
    nodes['A'] = head
    for i in range(1,5):
        # 节点添加进字典，方便复杂关系指针
        index.next = ComplexNode(val=valList[i])
        nodes[valList[i]] = index.next
        index = index.next
    nodes['A'].sibling = nodes['C']
    nodes['B'].sibling = nodes['E']
    nodes['D'].sibling = nodes['B']
    return head

def copyComplexChain(head:ComplexNode):
        if not head:
            return
        copyHead = ComplexNode(head.val)
        origin = head.next
        now = copyHead
        mirror = {}  # 存储新旧节点对应关系  key=旧节点，value=新节点
        mirror[head] = copyHead
        # 先初始化一个单链，新旧节点对应关系存入数据
        while origin != None:
            now.next = ComplexNode(origin.val)
            now = now.next
            mirror[origin] = now
            origin = origin.next

        # 接下来处理 sibling
        origin = head
        while origin != None:
            if origin.sibling != None:  #老节点有sibling
                node = mirror[origin]  #老节点对应的新节点
                sibling = mirror[origin.sibling]  #老节点的sibling对应的 新节点
                node.sibling = sibling  #sibling 挂载上
            origin = origin.next
        return copyHead

def copyComplexChain2(head:ComplexNode):
    # 1 复制 原节点N 的 复制节点N' 并连在 N 后
    pNode = head
    while pNode is not None:
        pCloned = ComplexNode(pNode.val)

        pCloned.next = pNode.next
        pNode.next = pCloned

        pNode = pCloned.next

    # 2 若原链有 A -> C, 则让复制节点有 A' -> C'
    pNode = head
    while pNode is not None:
        pCloned = pNode.next

        if pNode.sibling is not None:
            pCloned.sibling = pNode.sibling.next

        pNode = pCloned.next

    # 3 将原节点和复制的节点拆开，各自组成新链，那么复制节点的数值和关系和原链一致
    pNode = head
    pClonedHead = None
    pCloned = None

    if pNode is not None:
        pClonedHead = pCloned = pNode.next
        pNode.next = pCloned.next
        pNode = pNode.next
    # 这里步骤不记得就再拿纸画一遍，就ok了
    while pNode is not None:
        pCloned.next = pNode.next
        pCloned = pCloned.next
        pNode.next = pCloned.next
        pNode = pNode.next

    return pClonedHead



nodes = {}
copyNodes = {}
head = creatComplexChain()
def printChain(head:ComplexNode):
    while head != None:
        print(head.val, end='\t')
        head = head.next
printChain(head)
print()
print(nodes['A'].sibling.val)
print(nodes['B'].sibling.val)
print(nodes['D'].sibling.val)

copyHead = copyComplexChain2(head)
printChain(copyHead)
print()
print(copyHead.sibling.val)
print(copyHead.next.sibling.val)
print(copyHead.next.next.next.sibling.val)
print('把复制链第一节点的sibling改为第二节点，检查原链受不受影响')
copyHead.sibling = copyHead.next
print('原链：应是C，实际是：',head.sibling.val)
print('复制链：应是B，实际是：',copyHead.sibling.val)