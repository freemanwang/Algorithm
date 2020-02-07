'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
'''
# 最大就是255，所以不会有552这样的分割
# 字符串用3个 '.' 分成 4 部分，每部分都是 0-255

# 先找第一部分，可能有1、2、3位
class Solution:
    def restoreIpAddresses(self, s: str) :
        if len(s) < 4 or len(s) > 12 or s[0] == 0:
            return []
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if len(s) > (4- len(path)) * 3:
            return
        # s 消耗完，且4段已凑齐
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        # 长在1-3之间
        for i in range(1,4):
            # 若剩余部分不够长，就continue直至 i 出范围后结束循环
            if i > len(s):
                continue
            number = int(s[:i])
            if str(number) == s[:i] and number <= 255:
                self.dfs(s[i:],path+[s[:i]], res)

s = "25525511135"
c = Solution()
res = c.restoreIpAddresses(s)
print(res)

arr = []
arr2 = 'hello'
print(arr+[arr2[2:]])