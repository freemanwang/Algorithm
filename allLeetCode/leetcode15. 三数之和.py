'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
'''
# 假设 三数之和要求为 0

# 思路1：暴力，3层循环，时间复杂度 n**3

#思路2：依次遍历，遍历到某个数 n，将其转化为 两数之和 问题，即除该数外剩下的元素满足 2个数和为 -n。遍历为n，二数和最优为n，综合来说时间复杂度最好是 n**2

#思路3：2层循环得出所有2数和sum，然后查 sum 是否在 list 中。和思路2有相似之处。T=O(n**2)

# 思路4：sort.find.不好描述， 就是先排序，然后从头开始逐个遍历。
        先选一个元素为a，然后在它后面的序列的2端分别为b和c，计算 sum = a+b+c
        4.1如果 sum>0, 说明元素大了，因为有序，把c左移一位，继续求和比0
        4.2如果 sum<0，说明元素小了，同理，把b右移一位，继续
        4.3上面2步一直执行到b，c相遇，如果都没合法结果，就换a为下一个
        如果找到sum=0，那就ok，找不到的话，把右侧元素当a继续遍历，直到找到或者最后3个元素分别为a，b，c都不行，那只能False
        排序n，每次遍历又是n，时间复杂度综合是 n**2，好处在于空间复杂度低，2，3都需要n的空间复杂度；但这个的坏处是不好理解，想不到      
'''

# 思路3
def threeSum(nums:list):
    res = []
    nums.sort()
    if nums[0] > 0:
        return []
    end = 0
    while nums[end] < 0:
        end += 1
    # print(nums[:end+1])
    for i in range(end+1):
        target = -nums[i]
        hash_map = {}
        for index, value in enumerate(nums):
            if target - value in hash_map:
                tmp = sorted([nums[i], value, nums[hash_map[target-value]]])
                if tmp not in res:
                    res.append(tmp)
            hash_map[value] = index
    return res

# 思路4的 夹逼法
def threeSum2(nums:list):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        # 起始数就>0,不可能和为0
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1

        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1

nums = [-1, 0, 1, 2, -1, -4]
res = threeSum(nums)
print(res)

# nums.sort()
# print(nums)

l1 = [1,2,3]
l2 = [2,1,3]
l3 = [1,3,2]
print(l1==l2)
print(l3==l2)
print(l3==l1)