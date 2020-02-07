#给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

def letterCombinations(digits: str):
    if not digits or type(digits)!=str:
        pass
    # 如果输入str里有非数字，输入不合法立即结束
    if not digits.isdigit():
        return
    # 输入里有0或1，同样退出
    if digits.find('0')!=-1 or digits.find('1')!=-1:
        return
    # 做个2-9数字对应的映射，下标就是对应按键上的字母
    map = ['', 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    num = list(digits) #字符串按单个字符分成数组，如234=》[2,3,4]
    code = [] #存放各数字初步映射后所有可能的字符组数组，比如23就是['abc','def]
    for t in num:
       if map[int(t)]:
           tmp = list(map[int(t)])
           code.append(tmp)
    print("可匹配字母数组为",code)

    #这里想不起来就debug
    for index in range(1,len(code)):
        tmp = code[0][:]
        # print("可匹配字母数组为2", code)
        for x in tmp:
            for y in code[index]:
                # print(len(code[0]),code[0],type(code[0]))
                code[0].append(x+y)
            del code[0][0]
    return code[0]
    print('下面不会执行')
    return result




t = '234'
arr = letterCombinations(t)

print("所有拼接可能性：",arr)

# # 废弃版
#
# #给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# #给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# '''
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# '''
#
# def letterCombinations(digits: str):
#     if not digits or type(digits)!=str:
#         pass
#     # 如果输入str里有非数字，输入不合法立即结束
#     if not digits.isdigit():
#         return
#     # 输入里有0或1，同样退出
#     if digits.find('0')!=-1 or digits.find('1')!=-1:
#         return
#     # 做个2-9数字对应的映射，下标就是对应按键上的字母
#     map = ['', 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
#     num = list(digits) #字符串按单个字符分成数组，如234=》[2,3,4]
#     code = [] #存放各数字初步映射后所有可能的字符组数组，比如23就是['abc','def]
#     for t in num:
#        if map[int(t)]:
#            code.append(map[int(t)])
#     print("可匹配字母数组为",code)
#     result = comb(code)
#     return result
#
# # def comb(code:list):
# #     # 计算第一个元素和第二个元素的组合，将其存放在一临时变量里，
# #     # 全部穷举完后把结果替换原1，2项，继续新的1，2项的穷举匹配
# #     arr = code[:]
# #     tmp = []
# #     # 遍历arr[0]内各字母
# #     for i in range(len(arr[0])):
# #         # 遍历arr[1]内各字母
# #         for j in range(len(arr[1])):
# #             # 拼接
# #             tmp.append(arr[0][i] + arr[1][j])
# #         # 把存了所有拼接后的结果的tmp数组用来替换完成拼接的前2个元素
# #     arr = arr[2:]
# #     arr.insert(0, tmp)
# #     print("tmp",len(tmp),tmp)
# #     print("arr",len(arr),arr)
# #     # 剩余元素多余1个，就继续遍历拼接
# #     if len(arr) > 1:
# #         comb(arr)
# #     else:
# #         print("这里执行了")
# #         print(len(arr),len(arr[0]),arr[0])
# #         return tmp  #最后的tmp其实就是所有拼接的结果，也就是arr[0]
# #         return res
# # # 返回所有拼接的结果，我觉得和上行返回 tmp 一样，但实际并不一样，很奇怪
# # #     print('这行不该执行')
# #     print("返回的arr[0]:",len(arr), arr[0])
# #     return arr[0]
#
#
#
# t = '234'
# arr = letterCombinations(t)
#
# print("所有拼接可能性：",arr)
#
# # code = [1,2,3,4,5]
# # code = code[2:]
# # code.insert(0, 10)
# # print(code)
#
# def test():
#     for i in range(5):
#         for j in range(5):
#             print(f'{i}{j}',end='\t')
#
#         if j ==3:
#             return j
#         else:
#             return i
#
# t = test()
# print(t)