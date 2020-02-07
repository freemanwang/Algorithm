'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。
返回滑动窗口最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：
你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

进阶：
你能在线性时间复杂度内解决此题吗？
'''


# 设计思想是：用window记录一个窗口，滑动过程中，始终保持当前窗口内最大的元素的下标在最左侧，右侧新滑进窗口的元素加进窗口，如果它比之前的max大，那就清理它左侧所有；没之前max大的话就简单的加进来，观察
# 此算法高效，O(N)
def maxSlidingWindow1(nums:list, k:int):
    if not nums:
        return []
    window = []  # 存放下标
    res = []
    for index, item in enumerate(nums):
        if index >=k and window[0] <= index-k: #window前面大小超出窗口的元素去除
            window.pop(0)
        while window and nums[window[-1]] <= item:
        #如果新进元素item 是最大的，清除前面所有原有的元素，仅保留最大值的下标在window内
            window.pop()
        window.append(index) #最大值下标进window
        if index >= k - 1:
            res.append(nums[window[0]]) #窗口挪动时，不同的最大值加入res
    return res

# 此算法思路明了，但时间复杂度高， n**2,leetcode运行结果也证实了这点
def maxSlidingWindow2(nums:list, k:int):
    if not nums:
        return []
    res = []
    for start in range(len(nums) - k + 1):
        maxNum = max(nums[start:start+k])
        res.append(maxNum)
    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = maxSlidingWindow2(nums, k)
print(res)
