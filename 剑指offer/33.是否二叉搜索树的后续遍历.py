#如果是后续遍历，那么最末尾元素是根，根左侧全比根小，右侧全比根大

def isPostOrder(lst:list, length:int):
    if not lst or length <= 0:
        return False
    root = lst[length-1]

    i = 0
    while i< length - 1:
        # 这里是根的左子树，应全比根小
        if lst[i] > root:
            break
        i += 1
    j = i
    while j < length -1:
        # 这里是根的右子树，应全比根大
        if lst[j] < root:
            return False
        j += 1

    # 能运行到这里，根处没问题，递归其左右子树
    # 递归左子树
    left = True
    if i > 0:
        left = isPostOrder(lst, i)
    # 递归右子树
    right = True
    if i < length - 1:
        right = isPostOrder(lst[i:], length-i-1)
    # 左右子树都是二叉搜索树，此树才是二叉搜索树
    return left and right

lst = [5,7,6,9,11,10,8]
print(isPostOrder(lst,len(lst)))