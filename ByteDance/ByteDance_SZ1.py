'''
实现一个函数，要求去除一个字符串中倒数第二个指定字符，如去除字符串 'Hello world' 中倒数第二个字符 'o'，函数返回 'Hell world'
'''
s = "Hello world"
def solution(s:str, char:str):
    if not s:
        return
    if not str:
        return s
    index1 = s.rfind(char)
    print(index1)
    index2 = s.rfind(char, 0,index1)
    print(index2)
    # del s[index2]  #字符串没有 del 方法，切记
    new_s = ''
    for i in range(len(s)):
        if i != index2:
            new_s += s[i]
    return new_s

s = "Hello world"
res = solution(s,'o')
print (res)

s = 'abcde'
i = s.rfind('a',1,4)
print(i)