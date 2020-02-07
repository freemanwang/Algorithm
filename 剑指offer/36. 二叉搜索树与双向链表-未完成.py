from BinarySearchTree import *

def convert(root:Node):
    preNode = Node('TMP')
    convertNode(root,preNode)
    # 转换完后需返回有序双向链的头节点
    head = preNode
    while head is not None and head.left is not None:
        head = head.left

    return head

def convertNode(root:Node, preNode:Node):
    if root is None:
        return
    pCurrent = root

    # 遍历到最左侧叶子
    if pCurrent.left is not None:
        convertNode(pCurrent.left, preNode)

    # 左侧指针指向前一个遍历的节点（中序遍历，数值非严格递增，后遍历到的>=前遍历的）
    # （初始时preNode是None，也就是有序双向链第一个节点左指针为空，因为没有比它小的）
    # 再后面， left 就指向前一个遍历的，比当前遍历到的节点小的元素
    pCurrent.left = preNode

    # 有序双向链最后节点右指针指向当前中序遍历时的中间元素
    if preNode is not None:
        preNode.right = pCurrent

    # 中间元素成为有序双向链上最后一个元素
    preNode = pCurrent

    # 遍历右侧子树
    if pCurrent.right is not None:
        convertNode(pCurrent.right, preNode)

def printDeque(head:Node):
    while head is not None:
        print(head.val,end='=>')
        head = head.right
    print()

lst = [10,20,25,16,6,17,11,8,5]
root = creatBSTree(lst)
printBSTreeSeq(root)

head = convert(root)
print(head)
printDeque(head)
print(type(head))
# print(head.left.val)