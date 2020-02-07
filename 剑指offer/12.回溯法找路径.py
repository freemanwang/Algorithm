#12.回溯法判断是否有符合条件的路径

#字符矩阵
matrix = [
    ['a', 'b', 't', 'g'],
    ['c', 'f', 'c', 's'],
    ['j', 'd', 'e', 'h']
]

#要查询的路径
string = 'bfce'
visited = []
#生成 3*4 的矩阵，值全初始化为False
i,j = 0,0
for i in range(0,3):
    visited.append([])
    for j in range(0,4):
        visited[i].append(False)

# 每个元素作为起点开始检查
def hasPath(matrix:list, rows:int, cols:int, string:str):
    if not matrix or rows<1 or cols<1 or not string:
        return False
    index = 0
    for row in range(0,rows):
        for col in range(0,cols):
            if hasPathCore(matrix, visited, rows, cols, row, col, string, index):
                return True

#这里是实际的开始检查，被递归调用
def hasPathCore(matrix:list, visited:list, rows:int, cols:int, row:int, col:int, string:str, index:int):
    if index == len(string):
        return True
    hsP = False
    if row>=0 and row<rows and col>=0 and col<cols and matrix[row][col]==string[index] and not visited[row][col]:
        # 输出检查的元素，供理解逻辑
        # print(string[index])
        index += 1
        visited[row][col] = True
        hsP = hasPathCore(matrix, visited, rows, cols, row, col-1, string, index) or \
              hasPathCore(matrix, visited, rows, cols, row-1, col, string, index) or \
              hasPathCore(matrix, visited, rows, cols, row, col+1, string, index) or \
              hasPathCore(matrix, visited, rows, cols, row+1, col, string, index)

        if not hsP:
            index -= 1
            visited[row][col] = False
    return hsP

def printRoad(rows:int, cols:int):
    index = 0
    for row in range(0,rows):
        for col in range(0,cols):
            if visited[row][col] == True:
                print(matrix[row][col],index,' '*4,end='')
                index+=1
            else:
                print(matrix[row][col]," "*5,end='')
        print()

def printVisited(rows:int, cols:int):
    index = 0
    for row in range(0,rows):
        for col in range(0,cols):
            if visited[row][col] == True:
                print(matrix[row][col],str(index).center(3,' '),' '*2,end='')
                index+=1
            else:
                print(matrix[row][col]," "*5,end='')
        print()


flag = hasPath(matrix,len(matrix),len(matrix[0]),string)
print(flag)
printRoad(len(matrix),len(matrix[0]))
print(visited)