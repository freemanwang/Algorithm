import re

def isNumeric(string: str):
    if not str:
        return False
    # length = len(string)
    indexOfDot = string.find('.')

    print(indexOfDot,type(indexOfDot))   ######################

    # 小数点前有内容，即整数部分不为0
    if indexOfDot > 0:
        # 整数部分
        intStr = string[0:indexOfDot]
        # string更新为 .以后的部分
        string = string[indexOfDot + 1:]

        print(intStr,string) #########################

        if not checkOperators(intStr):

            print(1)

            return False

        if not isDigit(intStr):

            print(2)

            return False

    # 如果有e，把小数部分和e后部分截取出来
    if 'e' in string:

        print(3)

        indexOfe = string.find('e')
        floatStr = string[0:indexOfe]
        estr = string[indexOfe + 1:]

        print(floatStr,estr)

        # 2部分是否全数字
        if floatStr.isdigit() and isDigit(estr) and checkOperators(estr):
            return True
        return False

    elif 'E' in string:
        indexOfe = string.find('E')
        floatStr = string[0:indexOfe]
        estr = string[indexOfe + 1:]
        if not floatStr.isdigit and isDigit(estr) and checkOperators(estr):
            return True
        return False

    # 没有e，那string就是纯小数，必须得是纯数字
    if string.isdigit():
        return True
    return False


def isDigit(str):
    str = str.replace('+', '')
    str = str.replace('-', '')
    print('isDigit:',str)
    return str.isdigit()


def checkOperators(str):
    # 题目说 +-  -+ 存在的话，就不是数字了.理解成，超过1个以上的  + 或 -，或者非首位是+-，就不是数字
    pt1 = '.*(\+)|(\-).*'
    res = re.findall(pt1, str)
    count = 0
    for t in res:
        if t[0]:
            count += 1
        elif t[1]:
            count += 1
        if count > 1:
            return False
    if count != 0:
        # 只有一个 + -，判断首字符是不是 + -
        if str[0] != '+' and str[0] != '-':
            print('str[0]',str[0])
            return False
    return True

string = '-123.45e+6'
print(isNumeric(string))