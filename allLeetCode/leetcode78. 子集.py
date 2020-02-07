'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

# 方法1：迭代
def subSets1(nums:list):
    res = [[]]
    # 这里的逻辑，想不通debug一下就知道了
    for i in nums:
        res = res + [ [i] + num for num in res ]
    del res[0] # 删掉 []
    return res


# 方法2： 递归
def subSets2(nums:list):

    pass


# 方法3：
def subSets3(nums:list):
    if not nums:
        return
    # nums = str(nums)
    # print(nums)
    res = []
    subSets3Core([], nums, res)
    return res

def subSets3Core(selected, rest,res:list):
    if not rest or len(rest) == 0:
        res.append(selected)
        return
    subSets3Core(selected.append(rest[0]), rest[1:], res)
    subSets3Core(selected, rest[1:], res)



# def subSets3K(nums:list,k:int, res:list):
#     # 输入不合法
#     if not nums or k > len(nums):
#         return
#
#     # 需要选的数量和现存的数量一样，直接返回，这个是边界条件
#     if len(nums) == k:
#         return nums
#
#     # 第一个元素选或不选有2个分支，把2个分支得到的结果相加返回即可
#     res.append([].append(nums[0]).extend(subSets3K(nums[1:], k-1, res)))  #第一个选
#     res.append(subSets3K(nums[1:], k, res))    #第一个不选


lst = [1]
print(lst,type(lst))
print(lst[1:],type(lst[1:]))

nums = [1,2,3]
# res = subSets1(nums)
# print(res)
nums = "123"
res2 = subSets3(nums)
print(res2)
# s = str(nums)
# print(type(s),s)