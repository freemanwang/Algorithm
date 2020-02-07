#比较2个二叉树是否完全相等
import BinaryTree as BTree
lst1 = [1,2,3]
lst2 = [1,2,4]
tree1 = BTree.creatBTree(lst1)
tree2 = BTree.creatBTree(lst2)
def isEqual(tree1,tree2):
    # 2者都空
    if not tree1 and not tree2:
        return True
    # tree1 和 tree2 一个空一个非空
    if (not tree1 and tree2) or (tree1 and not tree2):
        return False
    # 2者都非空，判断数据相等不
    if tree1.data == tree2.data:
        # 数据相等的话，递归判断其子树
        return isEqual(tree1.lchild,tree2.lchild) and isEqual(tree1.rchild,tree2.rchild)
    return False

BTree.printTree(tree1)
BTree.printTree(tree2)
print(isEqual(tree1,tree2))