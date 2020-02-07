class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root:Node):
    print(f"根节点：{root.val}")
    que = []
    que.append(root)
    while len(que):
        node = que.pop(0)
        if node.left:
            que.append(node.left)
            print(f"{node.val}的左孩子：{node.left.val}")
        if node.right:
            que.append(node.right)
            print(f"{node.val}的右孩子：{node.right.val}")
    print(f"输出结束")
    return

def creatBTree(lst):
    index = 0
    leng = len(lst)
    root = Node(lst[index])
    # print(root.val,root.left,root.right)
    index += 1
    que = [root]
    while index < leng:
        node = que.pop(0)
        if lst[index] != None:
            child = Node(lst[index])
            node.left = child
            que.append(child)
        index += 1
        if lst[index] != None:
            child = Node(lst[index])
            node.right = child
            que.append(child)
        index += 1
    return root
def getDepth(tree:Node):
    if tree.val == None:
        return 0
    h1 = 0
    h2 = 0
    if tree.left:
        h1 = getDepth(tree.left)
    if tree.right:
        h2 = getDepth(tree.right)
    return max(h1,h2)+1

def preOrder(tree:Node):
    # 空树
    if not tree:
        return
    print(tree.val, end='\t')
    preOrder(tree.left)
    preOrder(tree.right)
    return

def inOrder(tree:Node):
    # 空树
    if not tree:
        return
    preOrder(tree.left)
    print(tree.val, end='\t')
    preOrder(tree.right)
    return

def postOrder(tree:Node):
    # 空树
    if not tree:
        return
    preOrder(tree.left)
    preOrder(tree.right)
    print(tree.val, end='\t')
    return

# lst = [8,6,10,5,7,9,11]
# tree = creatBTree(lst)
# printTree(tree)
# preOrder(tree)
# inOrder(tree)
# postOrder(tree)




