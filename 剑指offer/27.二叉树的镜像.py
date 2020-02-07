import BinaryTree as BTree
import copy
lst = [8,6,10,5,7,9,11]
tree = BTree.creatBTree(lst)
BTree.printTree(tree)

def switch(node:BTree.Node):
    # 两侧都为空
    if not node.lchild or not node.rchild:
        return

    # 两侧都有孩子
    if node.lchild and node.rchild:
        temp = copy.deepcopy(node.lchild)
        node.lchild = node.rchild
        node.rchild = temp
    # 仅左侧有孩子
    if node.lchild and not node.rchild:
        node.rchild = node.lchild
        node.lchild = None

    #     仅右侧有孩子
    if not node.lchild and node.rchild:
        node.lchild = node.rchild
        node.rchild = None

def mirrorRecur(tree:BTree.Node):
    # 树为空，没什么好镜像的
    if not tree:
        return
    # 仅根节点，也没什么好镜像的
    if not tree.lchild and not tree.rchild:
        return
    switch(tree)
    mirrorRecur(tree.lchild)
    mirrorRecur(tree.rchild)

mirrorRecur(tree)
BTree.printTree(tree)