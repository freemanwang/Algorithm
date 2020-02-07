'''
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
示例 2：

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
示例 3：

输入：[1]
输出：false
解释：没有满足要求的分组。
示例 4：

输入：[1,1]
输出：true
解释：可行的分组是 [1,1]
示例 5：

输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]

提示：

1 <= deck.length <= 10000
0 <= deck[i] < 10000

'''

def hasGroupsSizeX(deck: list):
    if not deck:
        return
    deck = deck[:]
    print('输入数组',deck)
    deck.sort()
    countdic = {}
    numset = set()
    for t in deck:
        numset.add(t)
    for t in numset:
        countdic[t] = deck.count(t)
    print(countdic)
    mintime = min(countdic.values())
    print("min:",mintime)
    print('countdic.values()',countdic.values())
    if 1 in countdic.values():
        return False
    # 改成这样为了应对  [1,1,1,1,2,2,2,2,2,2],4个1可以拆分成2个[1,1]
    for t in range(2,mintime+1):
        for count in countdic.values():
            print(count,t)
            # 只要有一个不是倍数的，就退出
            if count % t != 0:
                break
            # 全是整数倍那就ok
            return True
    return False



    # for count in countdic.values():
    #     # print(count)
    #     for t in range(2,mintime+1):
    #         if count % mintime != 0:
    #         # return False
    #         # 改成这样为了应对  [1,1,1,1,2,2,2,2,2,2]
    #         if mintime%2 == 0 and count%2 != 0:
    #             return False
    #         elif count %2 == 0 and count%2 == 0:
    #             return False


deck = [1,1,1,2,2,2,3,3]
r = hasGroupsSizeX(deck)
print(r)
