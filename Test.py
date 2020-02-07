string = 'ABCD'
# print(string[2])

#下面函数不能判断字符串是否结尾，无法停止。py不用 '\0'  判断字符串是否结尾，应根据长度计算
def last():
    i=0
    while 1:
        if string[i] == '\0':
            return i
            i+=1
# print(last())


lst = ''
if not lst:
    print(1)
else:
    print(2)
#
# arr = list(0 for i in range(0,10))   #迷一样的生成法
# arr2 = list(i for i in range(0,10))   #迷一样的生成法
# # arr.append(1)
# # arr.append(2)
# print(arr)
# print(arr2)
#
# ch = 'A'
# print(ord(ch))

arr = [10, -8, 99, 27, -103]
print(max(arr))
import re
pt = '.*(\+\-)|(\-\+).*'
s = 'asd+-ba-+asdr++fwgasd--nkjf--'
res = re.findall(pt,s)
lst = []
for t in res:
    if t[0]:
       lst.append(t[0])
    if t[1]:
        lst.append(t[1])
print(lst)
s = s.replace('+','')
s = s.replace('-','')
print(s)