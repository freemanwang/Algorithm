def getMatrix(rows,cols):
    visited = []
    i,j = 0,0
    index = 1
    for i in range(0,rows):
        visited.append([])
        for j in range(0,cols):
            visited[i].append(index)
            index += 1
    # print(visited)
    return visited

def printMatrixCircle(matrix, rows, cols, start):
#   每次都从 [start, start]开始打印。打印一圈start+1
#   打印分4步
#   1.从左向右打一行，无要求,只要数组非空，哪怕就1个元素，也能打第一行
#   2.从上至下打一列，要求2行以上，即end_row > start_row
#   3.从右至左打一行，要求最少得2行2列，即end_col > start_col
#   4.从下至上打一列，要求最少3行2列，即end_row - 1 > start_row
    start_row = start
    start_col = start
    end_row = rows - 1 - start_row
    end_col = cols - 1 - start_col

#     1.从左至右打1行
    for i in range(start_col, end_col+1):
        print(matrix[start_row][i],end='\t')
#     2.从上至下打1列
    if start_row < end_row:
        for i in range(start_row+1, end_row+1):
            print(matrix[i][end_col],end='\t')
#     3.从右至左打一行
    if start_row < end_row and start_col < end_col:
        for i in range(end_col-1,start_col-1,-1):
            print(matrix[end_row][i],end='\t')
#     4.从下至上打一列
    if  start_row < end_row-1 and start_col < end_col:
        for i in  range(end_row-1,start_row,-1):
            print(matrix[i][start_col])

def printMatrixClockCircle(matrix, rows,cols):
    if not matrix or rows <=0 or cols <= 0:
        return
    start = 0
    while cols > start*2 and rows > start *2:
        printMatrixCircle(matrix,rows,cols,start)
        start += 1

matrix = getMatrix(4,4)
printMatrixClockCircle(matrix,4,4)