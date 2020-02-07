'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-substring-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
prog = re.compile(pattern)
result = prog.match(string)
等价于
result = re.match(pattern, string)
'''
def repeatedSubstringPattern(s: str) -> bool:
    if not s:
        return False
    n = len(s)
    # 从1 -- n/2,逐个当作是子串来比对符合不
    for i in range(1,n//2+1):
        # 首先得没剩余
        if n % i == 0:
            # 剩下如果一节一节得匹配的上
            substr = s[:i]
            j = i
            while j < n and s[j:j+i] == substr:
                j += i
            #     且匹配到最后截至地址是 s 的最末
            if j == n:
                return True
    return False

def resolveByRegExp(s:str) -> bool:
    import re
    pattern = r'^(\w+)\1+$'
    print(re.match(pattern, s))
    if re.match(pattern,s):
        return True
    else:
        return False


s = 'abab'
print(repeatedSubstringPattern(s))
print(resolveByRegExp(s))

# res = 5 / 2
# print(res)
import re
s = "i love you not because of who you are, but because of who i am when i am with you"
r1 = r'\b\w'
content = re.findall(r1,s)
print(content)

s="i love you not because 12sd 34er 56df e4 54434"
r2 = r'\b\d'
r3 = r'\b\d+'
content = re.findall(r2,s)
content2 = re.findall(r3,s)
print(content)
print(content2)