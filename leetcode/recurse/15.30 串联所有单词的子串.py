'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
'''

class Solution:
    def findSubstring(self, s: str, words: list)  :
        if not s or not words:
            return []
        worddict = {}
        for t in words:
            if t not in worddict:
                worddict[t] = 1
            else:
                worddict[t] += 1
        sl = len(s)   #原字符串长度
        wl = len(words[0]) #单个单词长度
        n = len(words)  #共n个单词要匹配
        strl = wl * n  #匹配串长度
        res = []
        # 所有有可能匹配的串都检查
        for start in range(sl - wl*n + 1):
            tmpworddict ={}
            substr = s[start:start+strl]
            i = 0
            # 从长度考虑还有可能匹配上时
            while i + wl <= strl:
                # 如果单词匹配
                if substr[i:i+wl] in worddict:
                    if substr[i:i+wl] in tmpworddict:
                        tmpworddict[substr[i:i+wl]] += 1
                    else:
                        tmpworddict[substr[i:i + wl]] = 1
                    #后移一个单词位继续比较
                    i += wl
                # 子串长度是按着能完全匹配切片的，所以出现一个匹配就不可能匹配
                else:
                    break
            # 字典相等就是一个完全匹配
            if tmpworddict == worddict:
                #print('成功')
                res.append(start)
        return res


c = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
res = c.findSubstring(s,words)
print(res)
  
