# 1.笨办法
def getLongestSubStr(string:str):
    if not string:
        return
    if len(string) == 1:
        return 1
    length = len(string)
    # 初始化空子串、长为0的计数器
    subStr = []
    count = 0
    for i in range(length):
        if not (string[i] in subStr):
            subStr.append(string[i])
            count += 1
        else:
            return count
    #  能执行到这里说明批完完string都无重复
    if count == length:
        return count

string = 'abcdefghijklmnopqrstuvwxyz'
# string = "aaaaaaaaaaaaa"
# string = ''
t = getLongestSubStr(string)
print(t)

# 2.滑动窗口
def getLongestSubStrByWindow(string:str):
    if not string:
        return
    length = len(string)
    sets = set()
    count = 0
    i,j = 0,0
    while i < length and j < length:
        if string[j] in sets:
            sets.discard(string[i])
            i += 1
        else:
            sets.add(string[j])
            j += 1
            count = max(count, j-i)
    return count

tt = getLongestSubStrByWindow(string)
print(tt)



# sets = set()
# print(sets,type(sets))
# sets.add('alice')
# print(sets,type(sets))

