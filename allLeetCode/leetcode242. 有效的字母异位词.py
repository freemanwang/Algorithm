'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''

# 思路1： 若输入长度相同，那把输入先排序，然后逐一对比各字母。排序是T=O(nlogn)，遍历是n，综合来讲时间复杂度 T = O(nlogn)
def isAnagram(s:str, t:str):
    return sorted(s) == sorted(t)

# 思路2：对每个字符串建一个map，存储个字符出现次数；全统计完后若2map相同，那就True
#     时间复杂度：T = O(n),因为需要遍历所有元素，插入是O(1)

def isAnagram3(s:str, t:str):
    if (not s and t) or (s and not t):
        return False
    if not s and not t:
        return True
    if len(s) != len(t):
        return False

    maps, mapt = {}, {}

    for i in range(len(s)):
        if s[i] not in maps:
            maps[s[i]] = 1
        else:
            maps[s[i]] += 1
        if t[i] not in mapt:
            mapt[t[i]] = 1
        else:
            mapt[t[i]] += 1

    if mapt == maps:
        return True
    return False

lst = [1,9,23,41,66]
t = sorted(lst)
print(type(t),t)

