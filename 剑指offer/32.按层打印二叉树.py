from BinaryTree import *
# import queue
lst = [8,6,10,5,7,9,11]
tree = creatBTree(lst)
def printTreeByLevel(root:Node):
    #1.输入检测
    if not root:
        return

    #2算法开始
    queue = []
    queue.append(root)
    nextLevel = 0
    toBePrint = 1
    #队列非空时
    while len(queue) > 0:
        node = queue.pop(0)
        # 打印当前节点且不换行
        print(node.data,end='\t')
        if node.lchild:
            queue.append(node.lchild)
            nextLevel += 1
        if node.rchild:
            queue.append(node.rchild)
            nextLevel += 1
        #待输出量-1
        toBePrint -= 1
        if toBePrint == 0:
            #打印换行，切换到下一行
            print()
            toBePrint = nextLevel
printTreeByLevel(tree)
#换行
print()

def preOrderS(root:Node):
    '''
    前序遍历，非递归操作。用栈来辅助
    :param root: 根节点
    :return: 是否成功打印
    '''
    if not root:
        return False
    stack = []
    node = root
    print('前序非递归：')
    while node or len(stack):
        if node:
            stack.append(node)
            print(node.data,end='\t')
            node = node.lchild
        else:
            node = stack.pop()
            node = node.rchild
    print()

preOrderS(tree)


def inOrderS(root:Node):
    if not root:
        return
    stack = []
    node = root
    print('中序非递归：')
    while node or len(stack):
        if node:
            stack.append(node)
            node = node.lchild
        else:
            node = stack.pop()
            print(node.data,end='\t')
            node = node.rchild
    print()

inOrderS(tree)


# def postOrderS(root:Node):
#     if not root:
#         return
#     stack = []
#     node = root
#     while node or len(stack):
#         if node:
#             stack.append(node)
#             node = node.lchild
#         else:
#             node = stack.pop()
#             node = node.rchild

def postOrderS2(root):
    if root == None:
        return
    # 存放左右节点
    stack1 = []
    # 存放中间节点
    stack2 = []
    node = root
    stack1.append(node)
    print('后序非递归：')
    #不理解的话，画个图就理解了
    # 这个while循环用户找到后续遍历的逆序，存在stack2中
    while stack1:
        node = stack1.pop()
        if node.lchild:
            stack1.append(node.lchild)
        if node.rchild:
            stack1.append(node.rchild)
        stack2.append(node)
    while stack2:
        print(stack2.pop().data,end='\t')
    print()
postOrderS2(tree)