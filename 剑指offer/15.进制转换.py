#A-Z表1-26，AA表27.。。给字符串求出表十进制多少

#PS:    ord(ch)  返回字符ch对应的ASCII码，数值0-255
#PPS:   chr(int)  返回整数int对应的字符，数值0-255

def char2Int():
    ch2Int = dict()
    index = 65
    num = 1
    for t in range(0,26):
        ch2Int[chr(index)] = num
        index += 1
        num += 1
    print(ch2Int)
    return ch2Int


def getNum(string:str):
    length = len(string)
    ch2Int = char2Int()
    #当前计算到了多少位，从右往左，该为值为 num * 26 ** count
    count = 0
    #总和
    sum = 0
    # 逆序算
    for index in range(length-1,-1,-1):
        # print(index,string[index])
        last = string[index]
        sum += ch2Int[last] * pow(26,count)
        count += 1
        # print(last)
    print(sum)
    return sum

getNum('AA')