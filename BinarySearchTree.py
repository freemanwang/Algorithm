# PS：删除未完成

class Node:
    def __init__(self,val=None):
        self.p = None
        self.left = None
        self.right = None
        self.val = val


def creatBSTree(lst:list):
    if not lst:
        return
    length = len(lst)
    root = Node(lst[0])
    for t in lst[1:]:
        insert(root,t)
    return root

def insert(root:Node, val):
    if not Node:
        return Node(val)
    if val <= root.val:
        if root.left:
            insert(root.left, val)
        else:
            node = Node(val)
            root.left = node
            node.p = root
    else:
        if root.right:
            insert(root.right, val)
        else:
            node = Node(val)
            root.right = node
            node.p = root

def printBSTree(root:Node):
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

def isBSTree(root:Node):
    # 遍历到页节点都没错，是搜索树
    if not root.left and not root.right:
        return True
    # 如果左侧大于跟或者右侧小于等于跟，非搜索树
    elif (root.left and root.val < root.left.val) or (root.right and root.val > root.right.val):
        return False
    else:
        flag = 1
        if root.left:
            flag = isBSTree(root.left)
        if root.right:
            return flag and isBSTree(root.right)
        return  flag

def printBSTreeSeq(root:Node):
    if not root:
        return
    if root.left:
        printBSTreeSeq(root.left)
    print(root.val,end='=>')
    if root.right:
        printBSTreeSeq(root.right)

def BSTSearchRecur(root:Node, val:int):
    # root == None 时返回None，代表无值为key的节点；或者返回对应值的节点
    if root == None or val == root.val:
        return root
    if val < root.val:
        return BSTSearchRecur(root.left, val)
    else:
        return BSTSearchRecur(root.right, val)

def BSTSearch(root:Node, val:int):
    while root is not None and root.val != val:
        if val < root.val:
            root = root.left
        else:
            root = root.right
    return root

def BSTMinValNode(root:Node):
    while root.left is not None:
        root = root.left
    return root

def BSTMinVal(root:Node):
    while root.left is not None:
        root = root.left
    return root.val

def BSTMaxVal(root:Node):
    while root.right is not None:
        root = root.right
    return root.val

def BSTMaxValNode(root:Node):
    while root.right is not None:
        root = root.right
    return root

def BSTSuccessor(node:Node):
    '''
    return input node's successor node in in-order
    :return: successor-node
    '''
    if node.right != None:
        return BSTMaxValNode(node.right)
    p = node.p

    # 这里配合图看好理解。思路是向上找，找到当node不是父节点右孩子，即node是父节点的左孩子，那中序遍历下一个就是父节点，返回父节点
    while p is not None and node == p.right:
        node = p
        p = p.p
    return p


def inOrderR(root:Node):
    if root is not None:
        inOrderR(root.left)
        print(root.val, '=>')
        inOrderR(root.right)

def preOrderR(root:Node):
    if root is not None:
        print(root.val, '=>')
        inOrderR(root.left)
        inOrderR(root.right)

# 删除未完成
def BSTDelete(root:Node, node:Node):
    # 待删除节点无子节点，直接删除
    if not node.left and node.right:
        if node == node.p.left:
            node.p.left = None
        else:
            node.p.right = None
        del node
    #  待删除节点仅有一侧子节点，将其子节点顶替其位置
    # node仅左侧有子节点
    elif node.left is not None and node.right is None:
        # node 是 父节点的左孩子
        if node == node.p.left:
            node.p.left = node.left
            node.left.p = node.p
        # node 是 父节点的右孩子
        else:
            node.p.right = node.left
            node.left.p = node.p
        del node
    # node仅右侧有子节点
    elif node.left is None and node.right is not None:
        if node == node.p.left:
            node.p.left = node.right
            node.right.p = node.p
        else:
            node.p.right = node.right
            node.right.p = node.p
        del node
    # 两侧均有子节点，那么用其 左子树最大节点 或 右子树最小节点 顶替位置都可以
    # 这里选用 左子树最大节点，该节点 一定没有 右子树
    else:
        # 找到替换节点
        replace = BSTMaxValNode(node.right)
        # 把替换节点父节点指向它的指针清除
        if replace == replace.p.left:
            replace.p.left = None
        else:
            replace.p.right = None
        # 替换
        if node == node.p.left:
            node.p.left = replace
        else:
            node.p.right = replace
        replace.p = node.p
        del node





lst = [10,20,25,16]
root = creatBSTree(lst)
printBSTree(root)
print(isBSTree(root))
# printBSTreeSeq(root)
suc = BSTSuccessor(root.right)
print(suc.val)
BSTDelete(root, root.right)
printBSTree(root)
print(root.left.val)


#
# tree = Node(10)
# tree.left = Node(12)
# tree.right = Node(18)
# print(isBSTree(tree))

