#给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
#重复出现的子串要计算它们出现的次数。
'''
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-binary-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s or len(s) == 0 :
            return 0
        length = len(s)
        count = 0
        for i in range(length-1):
            # 遍历字符串，找到一个01或者10的子串的第一位下标
            if s[i] != s[i+1]:
                count += 1
                # 从该子串向左及向右检索；要求左侧元素==s[i],右侧元素==s[i+1]
                l,r = i,i+1
                while True:
                    # 检查左侧和右侧，在不越界的情况下，发现一个相等那么寻找子串数+1
                    if s[l]==s[l-1] and l>0 and s[r]==s[r+1] and r<length-1:
                        count += 1
                        l -= 1
                        r += 1
                    else:
                        break
        return count

c = Solution()
# s = "00110011"
s = "10101"
count = c.countBinarySubstrings(s)
print(count)
















        # count = 0
        # # 只能长为2n的子串才有可能
        # # 起始检验点从字符串起始开始，截止到倒数第二位
        # length = 2
        # for i in range(len(s)-1):
        #     # 取长为2，4，6，8直至其越界
        #     while i+length <= length+1:
        #         substr = s[i:i+2]
        #         start,end = 0,len(substr)-1
        #         while (end -start) >= 1:
        #             # 未比到最后就必须比
        #             if substr[start] == substr[end]:
        #                 #
        #                 if start + 1 == end:
        #                     count += 1
        #                 start += 1
        #                 end -= 1

                    # else:
                    #     break
                    # # 能走到这里，


            # if substr:
            #     pass

# s = '12345'
# print(s[1:5])