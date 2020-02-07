def getLen(num:int):
    length = 4
    i = 1
    while True:
        if pow(2, i) > num:
            return length
            break
        i += 3

        length += 3

def getNumberOf1(num:int):
    count = 0
    flag = 1


    while(flag):
        if flag & num:
            count += 1
        flag << 1
    return count

# nums = getNumberOf1(9)
# print(nums)
# print(getLen(9))
print(15 & 1)