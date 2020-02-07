'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
'''
def findKthLargest(nums: list, k: int) -> int:
    if not nums:
        return
    if k < 0 or k > len(nums):
        return
    nums.sort()
    return nums[len(nums)-k]

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))


nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums,k))

# 如果要求比大小时，相等的数记1个，就是说 1，2，3，4，4，5，5 中第3大的数是3，而不是4
def findKthLargest2(nums: list, k: int) -> int:
    if not nums:
        return
    if k < 0 or k > len(nums):
        return
    nset = set(nums)
    numsdict = dict.fromkeys(nset,0)
    for t in nums:
        numsdict[t] += 1
    res = list(numsdict.keys())[len(numsdict.keys())-k]
    return res
    # print(numsdict.keys(),type(numsdict.keys()))
    # print(list(numsdict.keys())[-2])
    # print(numsdict)
    # nums.sort()
    # return nums[len(nums)-k]

res = findKthLargest2(nums,4)
print(res)

# lst = [1,1,2,2,3,4,5,5,5]
# s = set(lst)
# print(s)
# dic = dict.fromkeys(s,0)
# print(dic)