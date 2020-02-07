from BinaryTree import Node,printTree

# 从前序和中序建树
def BinaryTreeConstruct1(prelst:list, inlst:list):
    if not prelst or not inlst or len(prelst) != len(inlst):
        return

    root = Node(prelst[0])
    index = inlst.index(prelst[0])

    root.left = BinaryTreeConstruct1(prelst[1:index+1], inlst[:index])
    root.right = BinaryTreeConstruct1(prelst[index+1:], inlst[index+1:])

    return root

# 中、后 得 树
def BinaryTreeConstruct2(inlst:list, postlst:list):
    if not postlst or not inlst:
        return None

    root = Node(postlst[-1])
    index = inlst.index(postlst[-1])

    root.left = BinaryTreeConstruct2(inlst[:index], postlst[:index])
    root.right = BinaryTreeConstruct2(inlst[index+1:], postlst[index:-1])

    return root




prel = [1,2,4,7,3,5,6,8]
inl = [4,7,2,1,5,3,8,6]
psl = [7,4,2,5,8,6,3,1]
root = BinaryTreeConstruct1(prel,inl)
printTree(root)

root2 = BinaryTreeConstruct2(inl,psl)
printTree(root2)



