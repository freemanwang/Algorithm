'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。

示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
'''
# 应用动态规划解决问题
#状态转移：走到(m,n) 只能由 (m-1,n) 向右走一格 或者 (m,n-1) 向下走一格
# 最优子结构：F(m, n) = F(m-1, n) + F(m, n-1)
# 边界: 1.问题规模小到单行或单列了，但其中有 1 ，就走不通
#       2.2行2列的话， (1,0)或(0,1)各决定一条路通不通

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid[0])  #横坐标，或者说有多少列
        n = len(obstacleGrid)     #纵坐标，或者说有多少行
        return self.check(obstacleGrid, m, n)

    def check(self, obstacleGrid, m, n):
        # 2行2列的话
        if m == 2 and n == 2:
            # 出入口堵死
            if obstacleGrid[1][1] == 1 or obstacleGrid[0][0] == 1:
                return 0
            # 2 条路全堵
            elif obstacleGrid[0][1] == 1 and obstacleGrid[1][0] == 1:
                return 0
            # 仅堵1条
            elif obstacleGrid[0][1] == 1 or obstacleGrid[1][0] == 1:
                return 1
            else:
                return 2
        # 如果是单行或单列的话
        elif m < 2 or n < 2:
            if n < 2:
                # 单行有 1 就不行
                if 1 in obstacleGrid[n-1]:
                    return 0
                return 1
            else:
                #单列有 1 也不行
                for t in range(n):#检查受列
                    if obstacleGrid[t][0] == 1:
                        return 0
                return 1
        # 如果上面2种都不是，就递归缩小问题规模来算
        else:
            return self.check(obstacleGrid, m-1, n) + self.check(obstacleGrid, m, n-1)

# code = [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# code = [[0],[1]]
# code = [[0,1]]
code = [[0,0],[0,0]]
c = Solution()
res = c.uniquePathsWithObstacles(code)
print(res)