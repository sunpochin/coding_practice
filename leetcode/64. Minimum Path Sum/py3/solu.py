class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        maxrow = len(grid) - 1
        maxcol = len(grid[0]) - 1
        dp = [[0 for _ in (grid[0])] for _ in grid]
        # print('dp: ', dp)
        for row in range(maxrow, -1, -1):
            for col in range(maxcol, -1, -1):
                if (row == maxrow and col != maxcol):
                    # last row
                    dp[row][col] = grid[row][col] + dp[row][col+1]
                elif (col == maxcol and row != maxrow):
                    # last col
                    dp[row][col] = grid[row][col] + dp[row+1][col]
                elif (col != maxcol and row != maxrow):
                    # grids in the middle
                    dp[row][col] = grid[row][col] + min(dp[row+1][col], dp[row][col+1])
                else:
                    # rightmost and down most grid
                    dp[row][col] = grid[row][col]
        # print('dp: ', dp)
        return dp[0][0]


    # def minPathSum(self, grid: List[List[int]]) -> int:
        # Approach 2: Dynamic Programming 2D
        # Algorithm
        # We use an extra matrix dpdpdp of the same size as the original matrix. In this matrix, dp(i,j)dp(i, j)dp(i,j) represents the minimum sum of the path from the index (i,j)(i, j)(i,j) to the bottom rightmost element. We start by initializing the bottom rightmost element of dpdpdp as the last element of the given matrix. Then for each element starting from the bottom right, we traverse backwards and fill in the matrix with the required minimum sums. Now, we need to note that at every element, we can move either rightwards or downwards. Therefore, for filling in the minimum sum, we use the equation:

        # dp(i,j)=grid(i,j)+min⁡(dp(i+1,j),dp(i,j+1)) dp(i, j)= \mathrm{grid}(i,j)+\min\big(dp(i+1,j),dp(i,j+1)\big) dp(i,j)=grid(i,j)+min(dp(i+1,j),dp(i,j+1))

        # taking care of the boundary conditions.

        # brute force
        # m = len(grid) - 1
        # n = len(grid[0]) - 1
        # self.mincost = float(inf)
        
        # def traverse(pos, sum):
        #     newsum = sum + grid[pos[0]][pos[1]]
        #     # print('pos: ', pos, ', sum: ', newsum)
        #     if pos == [m, n]:
        #         self.mincost = min(self.mincost, newsum)
        #         # print('mincost: ', self.mincost)
        #         return
        #     if pos[0] + 1 <= m:
        #         newpos = [pos[0] + 1, pos[1] ]
        #         traverse(newpos, newsum)
        #     if pos[1] + 1 <= n:
        #         newpos = [pos[0], pos[1] + 1 ]
        #         traverse(newpos, newsum)
        
        # traverse([0, 0], 0)
        # return self.mincost
                    