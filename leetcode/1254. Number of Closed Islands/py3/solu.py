# [[0,0,1,1,0,1,0,0,1,0],
#  [1,1,0,1,1,0,1,1,1,0],
#  [1,0,1,1,1,0,0,1,1,0],
#  [0,1,1,0,0,0,0,1,0,1],
#  [0,0,0,0,0,0,1,1,1,0],
#  [0,1,0,1,0,1,0,1,1,1],
#  [1,0,1,0,1,1,0,0,0,1],
#  [1,1,1,1,1,1,0,0,0,0],
#  [1,1,1,0,0,1,0,1,0,1],
#  [1,1,1,0,1,1,0,1,1,0]]

# grid:  [
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
# [1, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Solution:
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, val):
            if 0<=i<m and 0<=j<n and grid[i][j]==0:
                grid[i][j] = val
                dfs(i, j+1, val)
                dfs(i+1, j, val)
                dfs(i-1, j, val)
                dfs(i, j-1, val)
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == 0:
                    dfs(i, j, 1)
        print('grid: ', grid)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 1)
                    res += 1
                    
        return res
            
#     def closedIsland(self, grid: List[List[int]]) -> int:
#         rowcnt = len(grid)
#         colcnt = len(grid[0])
        
#         def dfs(row, col):
#             if row < 0 or row >= rowcnt or col < 0 or col >= colcnt:
#                 return False
#             if grid[row][col] == 1:
#                 return True
#             if grid[row][col] == -1:
#                 return True
#             grid[row][col] = -1
#             # any of it return False would cause I return False
#             ret = dfs(row+1, col) and dfs(row-1, col) and dfs(row, col+1) and dfs(row, col-1)
#             return ret
        
#         sum = 0
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if 0 == grid[row][col] and True == dfs(row, col):
#                     sum += 1
        
#         return sum