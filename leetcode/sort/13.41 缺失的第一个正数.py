'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
'''
# 自己的解法
def firstMissingPositive(nums: list) -> int:
    if not nums:
        return 1
    nums = [elem for elem in nums if elem>0]

    # 去掉负数后如果数组长为0，那直接返回1
    if len(nums) == 0:
        return 1
    nums.sort()
    # 1不在的话，直接返回1
    if 1 not in nums:
        return 1
    print(nums)
    length = len(nums)
    for i in range(0,length):
        # 1 在的话，那就从1(下标0)开始累加1，直到有个能插的间隙
        if nums[i] - 1 > 0 and nums[i] - 1 not in nums:
            return nums[i] - 1
        if nums[i] + 1 > 0 and i + 1 < length and nums[i] + 1 < nums[i + 1]:
            return nums[i] + 1
        if i == length - 1:
            # 如果走到着，说明数组是1，2，3，4，5这样从1开始每个+1，那么只能返回末尾元素+1了
            # 那么第几个元素其实就等于几，于是返回最后一个元素的值+1，等价于下标i+1+1
            return nums[i] + 1

# lst = [1,2,0]
# lst = [3,4,-1,1]
# lst = [7,8,9,11,12]
# lst = [2]
# lst = [1,2,3,4,5]
# lst = [-1,-2,1,2,3,4]
# lst = [1,2,0]
# lst = [1,1]
# print(firstMissingPositive(lst))

# 老师的解法
def firstMissingPositive2(nums: list) -> int:
    if not nums:
        return 1
    nums = [elem for elem in nums if elem>0]

    # 去掉负数后如果数组长为0，那直接返回1
    if len(nums) == 0:
        return 1
    nums.sort()
    print(nums)
    length = len(nums)
    # 1不在的话，直接返回1
    if nums[0] != 1:
        return 1
    for i in range(0,length-1):
        # 1 在的话，那就从1(下标0)开始累加1，直到有个能插的间隙
        if nums[i+1] - nums[i] > 1:
            return nums[i]+1
    # 如果走到这，说明数组现有的元素无法插值，那就返回最末尾元素数值+1
    return nums.pop()+1

lst = [1,2,0]
# lst = [3,4,-1,1]
# lst = [7,8,9,11,12]
# lst = [2]
# lst = [1,2,3,4,5]
# lst = [-1,-2,1,2,3,4]
# lst = [1,2,0]
# lst = [1,1]
print(firstMissingPositive2(lst))