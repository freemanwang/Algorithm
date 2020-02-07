
def quickSort(lst:list):
    return qs(lst, 0, len(lst)-1)

def qs(lst, left, right):
    if left < right:
        pivot = Partition(lst, left, right)
        qs(lst, left, pivot - 1)
        qs(lst, pivot + 1, right)
    return lst

def Partition(lst, left, right):
    pivotKey = lst[left]

    while left < right:
        # 从右向左找到第一个比 中值 小的元素
        while left < right and lst[right] >= pivotKey:
            right -= 1
        # 找到的元素替换 中值 原位置，原来此处的元素存在 pivotKey
        lst[left] = lst[right]

        # 从左至右找到第一个大于 pivotKey 的元素
        while left < right and lst[left] <= pivotKey:
            left += 1
        # 把这个元素放到右边那个 比中值小 的元素位置
        lst[right] = lst[left]
        #总结来说，上门2个while就是在从左和从右找到了一个比中值大、小的元素换位

    # 然后最外层while继续，直到 pivotKey 这个中值左侧都比它小，右侧都比它大
    # 把 pivotKey 放中间
    lst[left] = pivotKey
    # 返回 中值 下标，便于递归两侧继续快排
    return left

lst = [2,63,22,5,9,32,54,8,13,32]
quickSort(lst)
print(lst)

def partiton(lst, left, right):
    pivotKey = lst[left]
    while left < right:
        while left < right and lst[right] >= pivotKey:
            right -= 1
        lst[left] = lst[right]

        while left < right and lst[left] <= pivotKey:
            left += 1
        lst[right] = lst[left]

    lst[left] = pivotKey
    return left

