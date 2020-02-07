def longestStr(s:str):
    if not s:
        return
    length = len(s)
    maxLen = 0
    start = 0
    for i in range(length):
        # 如果左右两侧各 + 1，依然是回文串的话
        if i - maxLen >= 1 and s[i-maxLen-1 : i+1] == s[i-maxLen-1 : i+1][::-1]:
            start = i - maxLen #记录起始位置
            maxLen += 2
            continue

        #  找到一个回文串，
        if i - maxLen >= 0 and s[i-maxLen-1 : i+1] == s[i-maxLen-1 : i+1][::-1]:
            start = i - maxLen  #


class Solution2:
    def __init__(self):
        self.max = 0
        self.maxLen = 0
        self.res = ''

    # 中心扩散法
    def longestStr1(self, s:str):
        if not s:
            return
        if len(s) == 0:
            return s

        length = len(s)
        # maxLen = 0
        start = 0
        for i in range(length):
            self.diff(s, i, i) # 以一个位置为中心，找奇数长度的, 'aba'类
            self.diff(s, i, i+1) #以2点来扩散，找偶数长度的，'abba'类
        return self.res



    # 比对以当前位置为中心可的最长回文串
    def diff(self, s:str, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > self.max:
                self.max = right - left + 1
                self.res = s[left:right+1]
            left -= 1
            right += 1

s = 'tababaads' #ababa
b = 'abbadasdq'   #abba
c = Solution2()
print(c.longestStr1(s))

c.res = ''
c.maxLen = 0
c.max = 0
print(c.longestStr1(b))