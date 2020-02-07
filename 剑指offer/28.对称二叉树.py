#检测二叉树是否对称，那么可以换一种遍历方法，来比对着遍历
#比如针对前序遍历，是中左右，那么我们写一个中右左，遍历时比较元素，全部一样就对称，否则不对称
import BinaryTree as BTree
def isSymmetrical(tree:BTree.Node):
    return check(tree,tree)

def check(root1:BTree.Node, root2:BTree.Node):
    # 左右同为空节点，对称
    if not root1 and not root2:
        return True
    # 如果左右一个空一个非空，那么下面的判别式为真。如果全非空，那么为假
    if (not root1 and root2) or (root1 and not root2) :
        return False
    # 走到这里，证明都非空，那就直接比数据
    if root1.data != root2.data:
        return False
    return check(root1.lchild, root2.rchild) and check(root1.rchild, root2.lchild)

tree = BTree.creatBTree([7,7,7,7,7])
print(isSymmetrical(tree))