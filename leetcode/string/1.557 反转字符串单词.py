#给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#输入: "Let's take LeetCode contest"
#输出: "s'teL ekat edoCteeL tsetnoc"
class Solution:
    def reverseWords(self,s:str) ->str:
        if not s or type(s) != str or len(s) == 0:
            print('err input')
            return False
        # 按单词切分
        arr = s.split(' ')
        res = []
        # print('arr:',arr)
        # 把每个单词逆转
        for item in arr:
            # 把单词切成字母组成的数组
            tarr = list(item)
            # 反转各单词字母
            tarr.reverse()
            # 拼回成单词
            tstr = ''.join(tarr)
            # 字母反转后的单词放回结果数组
            res.append(tstr)
        # print('res:', res)
        # 结果数组拼接成结果字符串
        res = ' '.join(res)
        print(res)
        return res

print(type('123'))
c = Solution()
s = "Let's take LeetCode contest"
c.reverseWords(s)

#单词拆成字母的方法有：
# 1 直接list类型转换
word = "alice"
s1 = list(word)
# 2 list 生成
s2 = [ch for ch in word]
# 3 循环创建list
s3 = []
for t in word:
    s3.append(t)

print(s1)
print(s2)
print(s3)