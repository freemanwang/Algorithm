'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
'''
from BinaryTree import *
class Solution(object):
    def isSymmetric(self, root:Node):
        if not root:
            return True
        return self.check(root,root)



    def check(self, root1:Node, root2:Node):
        # 都空
        if root1 is None and root2 is None:
            return True
        # 一空一非空
        if (not root1 and root2) or (root1 and not root2):
            return False
        # 都非空，那就比数据
        if root1.data != root2.data:
            return False
        # 数据相等，就递归比子节点
        return self.check(root1.lchild,root2.rchild) and self.check(root1.rchild,root2.lchild)
