import BinaryTree as btree
lst1 = [8,8,7,9,2,None,None,None,None,4,7]
lst2 = [8,9,2]
root1 = btree.creatBTree(lst1)
root2 = btree.creatBTree(lst2)
btree.printTree(root1)
btree.printTree(root2)

def isChildTree(root1, root2):
    # 2者只要有1个为空，False
    if not root1 or not root2:
        return False

    flag = isEqual(root1,root2)
    if not flag:
        flag = isChildTree(root1.lchild,root2)
    if not flag:
        flag = isChildTree(root1.rchild,root2)
    return flag


def isEqual(root1, root2):
    # 子树检查到叶节点了，全都对的上，所以True
    if not root2:
        return True
    # 子树没到叶，而树已到叶，显然False
    if not root1:
        return False

    # 当前节点值相等时，递归遍历子树，全等才True
    if root1.data == root2.data:
        return isEqual(root1.lchild,root2.lchild) and isEqual(root1.rchild,root2.rchild)
    else:
        return False

flag = isChildTree(root1,root2)
print(flag)