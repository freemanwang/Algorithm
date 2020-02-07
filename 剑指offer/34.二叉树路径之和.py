from BinaryTree import *

def findPath(root:Node,expectedSum):
    if not root:
        return
    path = []
    currentSum = 0
    findingPath(root,expectedSum, path, currentSum)

def findingPath(root:Node, expectedSum:int, path:list, currentSum:int):
    currentSum += root.data
    path.append(root.data)

    #如果是叶节点且本路径之和等于期望值，则打印
    isLeaf = False
    if not (root.lchild or root.rchild):
        isLeaf = True
    if currentSum == expectedSum and isLeaf:
        for t in path:
            print(t, end="\t")
        print()

    if root.lchild:
        findingPath(root.lchild,expectedSum,path,currentSum)
    if root.rchild:
        findingPath(root.rchild,expectedSum,path,currentSum)
#    返回父节点前需在路径上删除当前节点
    path.pop()

lst = [10, 5, 12, 4, 7]
root = creatBTree(lst)
expectedSum = 22
path = []
findPath(root,expectedSum)

# lst = [0,1]
# lst.append(2)
# print(lst)
# print(lst.pop())
# print(lst.pop(1))
