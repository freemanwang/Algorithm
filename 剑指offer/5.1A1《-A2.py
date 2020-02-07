a1 = [1,2,3,4,5]
a2 = [2,4,6,8,10]
#print(id(a1))
#a1.append(8)
#print(id(a1))
#a1地址没变

def a1uniona2(a1, a2):
    if not isinstance(a1,list) and not isinstance(a2,list):
        return
    if a1 == None or a2 ==None:
        return
    l1 = len(a1)
    l2 = len(a2)
    tlst = [None]*l2    #扩充至可容下a2
    a1.extend(tlst)
    index1 = l1 -1
    index2 = l2 -1
    newIndex = len(a1)-1
    while index2 >= 0:
        if a1[index1] > a2[index2]:
            if a1[newIndex] == None:
                a1[newIndex] = a1[index1]
                a1[index1]=None
                index1-=1
                newIndex-=1
            else:
                print('数据覆盖，逻辑有误')
        else:
            if a1[newIndex] == None:
                a1[newIndex] = a2[index2]
                index2-=1
                newIndex-=1
            else:
                print('数据覆盖，逻辑有误')

    print('A2插入A1完成')
    return

a1uniona2(a1,a2)
print(a1)