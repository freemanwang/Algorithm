matrix = [
    [1,2,8,0],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]
]

def search(matrix, num):
    if matrix == None:
        print('查无此矩阵')
        return
    sum = 0
    for t in matrix:
        sum += len(t)
    y = len(matrix)     #矩阵行数
    x = sum/y           #矩阵列数
    if x != y:
        print('输入的矩阵不正确')
        return
    rs = 0  #行起
    re = y-1  #行末
    cs = 0  #列起
    ce = int(x-1)  #列末
    if num < matrix[0][0] or num > matrix[re][ce]:  #矩阵中不可能有num就直接结束
        print('Too small or too big')
        return False
    flag = False
    while ce>=0 and rs <= y:

        if num < matrix[rs][ce]:
            ce -=1
        elif num > matrix[rs][ce]:
            rs += 1
        else:
            flag = True
            print('Found')
            return True
    # if flag:
    #     return True
    print('Not Found')
    return False

nullP = [[]]

search(matrix,12)   #ok
search(matrix,120)  #告知不在
search(nullP,1)     #可识别出输入有问题

