class Solution(object):
    # 解法1：1次hash法, T = O(n)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 注意：hash_map 中的数据是检查后不符合要求才添加进去的，换句话说就是如果能在hash_map里找到的元素不会和当前遍历到的元素是同一个，解决了一个数被多次使用的问题
        hash_map = dict()#存 数值 和 下标 对应关系
        for index,item in enumerate(nums):
            if target - item in hash_map:
                return [index, hash_map[target-item]]
            hash_map[item] = index



    # 解法2：暴力，2层循环   T = O(n**2)
    def brute(self, nums, target):
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[j] == target - nums[i]:
                    return [i, j]
                j += 1
            i += 1
        return []

    # 解法3：2遍哈希表， T = O(n)
    # 意思是先把数值和下标插入哈希表，检测时元素不能等于自身
    # 注意：这里的方法，和1次哈希不同。如果有冲突数据，那么hash_map里存的是最后一个的下标；不能避免一个数被多次用，所以加上了下标是否相同的检测，只有找到的符合条件的元素的下标和当前遍历元素的下标不同才有效
    def twoTimesHash(self, nums, target):
        hash_map = dict()
        for index, item in enumerate(nums):
            hash_map[item] = index

        for index, item in enumerate(nums):
            if target - item in nums and hash_map[target - item] != index:
                return [index, hash_map[target - item]]
        return []

    #如果希望返回的不是下标，而是数字
    def twoNums(self, nums, target):
        nums_dict = {}
        res = []
        for i, v in enumerate(nums):
            nums_dict[v] = i
        for i,v in enumerate(nums):
            if target - v in nums and nums_dict[target-v] != i:
               res.append([v,target-v])
        return res

# lst = [3,2,4,3,3]
# target = 6

lst = [2,7,7,11,2,11,15,7,2]
target = 17
c = Solution()
res = c.twoSum(lst, target)
print(res)


res2 = c.twoNums(lst, target)
print(res2)

def twoSum3(arr,target):
    hash = dict()
    for num in arr:
        if target-num in hash:
            return (num,target-num)
        else:
            hash[num] = target-num