'''
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：
输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。
示例 2：

输入：[5,5,10]
输出：true
示例 3：

输入：[10,10]
输出：false
示例 4：

输入：[5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。

提示：
0 <= bills.length <= 10000
bills[i] 不是 5 就是 10 或是 20 
'''

# 策略： 优先给金额大的零钱，尽量手里握有更多零钱，以备将来

def lemonadeChange(bills:list):
    box = []
    # 只要还有顾客
    while(len(bills)>0):
        money = bills.pop(0)
        if money == 5:
            box.append(money)
        else:
            change = money - 5
            if change == 5:
                if 5 in box:
                    i = box.index(5) #找到5块
                    del box[i]
                    box.append(10)
                else:
                    return False #没有5块可找，失败
            else:#该找15块
                # 优先找 10 + 5
                if 5 in box and 10 in box:
                    i1 = box.index(5) #找到5块
                    i2 = box.index(10) #找到10块
                    # i1 在 i2 前面，删 i1 对 i2 下标有影响
                    if i1 < i2:#删一个后i2下标-1
                        del box[i1]
                        del box[i2-1]
                    # i1 在 i2 后，不影响
                    else:
                        del box[i1]
                        del box[i2]

                    box.append(20)
                elif box.count(5) >=3:  #没10，有3个及以上的5，只能找3个5
                    box.remove(5)
                    box.remove(5)
                    box.remove(5)
                else:#没钱找就失败
                    return False
    # 全部顾客都搞定都没问题，自然True
    return True

# lst = [5,5,5,10,20]
# lst = [5,5,10]
# lst = [10,10]
lst = [5,5,10,10,20]
print(lemonadeChange(lst))


