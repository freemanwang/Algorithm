#假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，
# 花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
'''
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。
能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:

数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def canPlaceFlowers(flowerbed: list, n: int):
    # 输入非法
    if not flowerbed or n < 0:
        return False
    # n > 0的总数
    if n > flowerbed.count(0):
        return False
    length = len(flowerbed)
    index = 0
    while index < length:
        # # 第一个为1
        # if index == 0:
        #     if flowerbed[index] == 0 and index+1<l:
        #     index += 1
        #     continue

        #     中间位置
        # 当前位置及下一位都是0
        if flowerbed[index]==0 and index+1<length and flowerbed[index+1]==0:
            # index-1>0，意思是在1位及以后且前后一位都是0
            if index-1>=0 and flowerbed[index-1] == 0:
                flowerbed[index]  = 1
                n -= 1
                index += 1
            elif index-1 == -1:
                # index-1==-1，那么现在就在0位，且1位为0，可以种
                flowerbed[index] = 1
                index += 1
                n -= 1
            else:
                # 在1以后1前一位非0，不能种，后移一位继续检查
                index += 1

        #     当前在最后一位，且最后一个为0，且倒数第2个也为0
        elif index == length-1 and flowerbed[index]==0 and flowerbed[index-1]==0:
            flowerbed[index] = 1
            # 后移一位继续判断
            n -= 1
            index += 1

        #  在中间，且不满足当前和下一位都0，跳过当前和下一个
        else:
            index += 2
    if n > 0:
        return False
    return True

flowerbed = [0,0,1,0,1]

n = 1
print(canPlaceFlowers(flowerbed,n))
