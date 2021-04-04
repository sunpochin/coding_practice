#
# dfs search from any 1 grid, after touching a 1 grid, 
# set it to 0 to avoid duplicate counting.
#

# Time Complexity: O(R∗C), where R is the number of rows in the given grid, and CCC is the number of columns. We visit every square once.
# Space complexity: O(R∗C), the space used by seen to keep track of visited squares, and the space used by the call stack during our recursion.

# maintain a variable maxarea, when finished counting area
class Solution:
    def __init__(self):
        self.maxarea = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seenset = ()
        
        def dfs(row, col, grid):
            maxrow = len(grid) - 1
            maxcol = len(grid[0]) - 1
            # print('row, col: ', row, col)
            if row < 0 or row > maxrow or col < 0 or col > maxcol or grid[row][col] == 0:
                # print('return 0')
                return 0
            # visited, set to 0
            grid[row][col] = 0
            ret = 1 + dfs(row+1, col, grid) + dfs(row-1, col, grid)\
                + dfs(row, col+1, grid) + dfs(row, col-1, grid)
            return ret

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                area = dfs(row, col, grid)
                self.maxarea = max(self.maxarea, area)
        return self.maxarea

            
