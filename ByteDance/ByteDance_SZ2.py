'''
实现一个函数，输入两个二进制数字字符串，输出它们的二进制和

我分别实现了     二进制加        和          十进制加
'''



class Solution(object):
    # 两十进制数相加（字符串形式）的解决办法
    def addStrings10(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 and not num2:
            return num1
        if num2 and not num1:
            return num2

        # 调整至同样长
        resize = self.resize(num1, num2)
        num1 = resize[0]
        num2 = resize[1]
        # print(num1, num2)
        # 返回相加值
        return self.add10(num1, num2)

    def addStrings2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 and not num2:
            return num1
        if num2 and not num1:
            return num2

        # 调整至同样长
        resize = self.resize(num1, num2)
        num1 = resize[0]
        num2 = resize[1]
        # print(num1, num2)
        # 返回相加值
        return self.add2(num1, num2)


    def resize(self,num1, num2):
        len1 = len(num1)
        len2 = len(num2)

        # 给短的字符串前面补 0
        if len1 > len2:
            length = len(num1)
            for t in range(len1 - len2):
                num2 = '0' + num2
        else:
            for t in range(len2 - len1):
                num1 = '0' + num1
        # 返回处理后的2数
        return [num1,num2]

    def add10(self, num1, num2):
        res = []  # 结果
        # print('开始计算')
        length = len(num1)
        num1 = list(num1)
        num2 = list(num2)
        num1.reverse()  #逆序，相加，方便进位，然后输出结果时再逆回来
        num2.reverse()  #逆序，相加，方便进位，然后输出结果时再逆回来
        # print(num1, num2)
        toNext = 0  # 进位计数
        for i in range(length):
            tmp = int(num1[i]) + int(num2[i]) + toNext
            if tmp >= 10:
                toNext = tmp // 10  # 进位
                cur = tmp % 10  # 当前位
            else:
                cur = tmp  # 当前位
                toNext = 0  # 进位清零，消除残留影响
            res.append(str(cur))
        # 如果最高位有进位，一定要处理进来
        if toNext != 0:
            res.append(str(toNext))
        res.reverse()
        res = ''.join(res)

        return res

    # 二进制数字串相加
    def add2(self, num1, num2):
        res = []  # 结果
        length = len(num1)
        num1 = list(num1)
        num2 = list(num2)
        num1.reverse()  #逆序，相加，方便进位，然后输出结果时再逆回来
        num2.reverse()  #逆序，相加，方便进位，然后输出结果时再逆回来
        toNext = 0  # 进位计数
        for i in range(length):
            tmp = int(num1[i]) + int(num2[i]) + toNext
            if tmp >= 2:
                toNext = tmp // 2  # 进位
                cur = tmp % 2  # 当前位
            else:
                cur = tmp  # 当前位
                toNext = 0  # 进位清零，消除残留影响
            res.append(str(cur))
        # 如果最高位有进位，一定要处理进来
        if toNext != 0:
            res.append(str(toNext))
        res.reverse()
        res = ''.join(res)

        return res

# num1 = '2999'
# num2 = '3333'
# c = Solution()
# res = c.addStrings10(num1, num2)
# print(res)

num1 = '11'
num2 = '1'
c = Solution()
res = c.addStrings2(num1, num2)
print(res)


