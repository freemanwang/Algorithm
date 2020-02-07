'''
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gray-code
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 规律，输出具有对称性，输入为n，输出会有 2**n个，且高位是0，1的数是相等的
# 递归向上推，从n=2的输出，在首位分别+0和+1，就是n=3的输出
def grayCode(n: int):
    if n <= 0:
        return
    if n == 1:
        return ['0','1']
    else:
        # 递归求前一个grayCode
        pre = grayCode(n-1)
        #这里是存放结果的数组，必须先给初始化足够的位置，否则后面没法放
        # python不像JS，下标超出后会报错。
        result = [0 for t in range(2**n)]
        # 最大下标，n=3的话就是7，n=4就是15，以此类推，用来做+0和+1的辅助
        maxIndex = 2 ** n - 1
        index = 0
        # print(pre)
        l = len(pre)
        while index < l:
            result[index] = '0' + pre[index]
            result[maxIndex-index] = '1' + pre[index]
            index += 1
    # for i in range(len(result)):
    #     result[i] = int(result[i],2)
        return result

arr = grayCode(3)
print(arr)
