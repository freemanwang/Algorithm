def Permutation(s:str):
    if not s:
        return
    s = list(s)
    res = []
    PermutationCore(s,0,res)
    return res

# 思路是：以下标表示元素；把 0 和 1，2，3...后面的元素逐个交换，然后再递归把 1 和 2,3,...交换，这样递归下去，就是所有可能的组合
# 每次递归完一种可能，会再改回原样，再去递归下一步元素交换的顺序
def PermutationCore(s:list, start:int,res:list):
    # 调换到尾部了，那就作为一中结果，存进 res 数组
    if start == len(s) - 1:
        res.append(''.join(s))
    else:
        for i in range(start, len(s)):
            # 如果元素相同就不必交换了
            if i != start and s[i] == s[start]:
                continue
            # 调换位置
            s[i], s[start] = s[start], s[i]
            # 递归交换已交换的元素，从它下一位开始做子串继续调换
            PermutationCore(s, start+1,res)
            # 把调换改回去
            s[i], s[start] = s[start], s[i]

s = 'abc'
res = Permutation(s)
print(res)


# 获取长度不同的连续子串，记住，连续，所以没用 'ac'这样的
# T = O(n**2) 或许更多，因为 sorted
def subStr(s:str):
    if not s:
        return
    ss = list(s)
    res = set()
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            res.add(','.join(ss[i:i + j]))
    return res



res2 = subStr(s)
print(res2)