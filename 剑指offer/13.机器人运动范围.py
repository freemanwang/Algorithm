#可进入的方格下标各位之和小于给定值

def getVisitedMatrix(rows,cols):
    visited = []
    i,j = 0,0
    for i in range(0,rows):
        visited.append([])
        for j in range(0,cols):
            visited[i].append(False)
    print(visited)
    return visited

#从某一点（非边际点），可以上下左右各走一个，计算其坐标各位之和
def blockCount(rows, cols, ceil):
    if ceil<0 or rows<=0 or cols<=0:
        return 0
    visited = getVisitedMatrix(rows,cols)
    count = blockCountCore(ceil,visited, rows, cols, 0, 0)
    return count


def blockCountCore(ceil,visited,rows,cols,row,col):
    count = 0
    if row>=0 and row<rows and col>=0 and col<cols and getSum(row)+getSum(col)<=ceil and not visited[row][col]:
        visited[row][col] = True
        count = 1 + blockCountCore(ceil,visited,rows,cols,row,col-1) + \
                    blockCountCore(ceil, visited, rows, cols, row-1, col) + \
                    blockCountCore(ceil,visited,rows,cols,row,col+1) + \
                    blockCountCore(ceil,visited,rows,cols,row+1,col)
    return count

def getSum(num):
    sum = 0
    while num%10 != 0:
        sum += num%10
        num = num // 10
    return sum

count = blockCount(10,10,18)
print(count)  #100   每个都能能进。
#设成100*100矩阵时，递归导致栈爆了，无法测试
