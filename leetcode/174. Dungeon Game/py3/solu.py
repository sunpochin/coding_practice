#[[-2, -3, 3],
# [-5,-10, 1],
# [10, 30,-5]]

#[[7==5-(-2), 5==2-(-3), 2==5-3],
# [0, 0, 5==6-1],
# [1, 1==(6-30) if it >= 1 else 1, 6==1-(-5)]]


class Solution:
    # solu
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * cols for _ in range(rows)]
        def get_min_health(curcell, nextrow, nextcol):
            if nextrow >= rows or nextcol >= cols:
                return float('inf')
            nextcell = dp[nextrow][nextcol]
            return max(1, nextcell - curcell)
        
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                curcell = dungeon[row][col]
                right_health = get_min_health(curcell, row, col+1)
                down_health = get_min_health(curcell, row+1, col)
                next_health = min(right_health, down_health)
                print('row:', row, ', col:', col, ', right:', right_health, ', down:', down_health, ', next:', next_health, ', curcell: ', curcell)
                if next_health != float('inf'):
                    min_health = next_health
                else:
                    min_health = 1 if curcell >= 0 else (1-curcell)
                print('min: ', min_health)
                dp[row][col] = min_health
        print('dp: ', dp)
        return dp[0][0]
    
    # Return the knight's minimum initial health so that he can rescue the princess.
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         maxrow = len(dungeon) - 1
#         maxcol = len(dungeon[0]) - 1
#         print('maxrow: ', maxrow, ', maxcol: ', maxcol)
#         minhp = 1
#         dp = [[float('inf')] * (maxcol + 1) for _ in range(maxrow + 1)]
#         for row in reversed(range(maxrow + 1) ):
#             for col in reversed(range(maxcol + 1) ):
#                 if (row == maxrow and col < maxcol):
#                     if (dp[row][col+1] - dungeon[row][col] >= 1):
#                         dp[row][col] = dp[row][col+1] - dungeon[row][col]
#                     else:
#                         dp[row][col] = 1
#                 elif (row < maxrow and col == maxcol):
#                     hp = dp[row+1][col] - dungeon[row][col] 
#                     if (hp >= 1):
#                         dp[row][col] = hp
#                     else:
#                         dp[row][col] = 1
#                 elif (row < maxrow and col < maxcol):
#                     fromrow = 0
#                     hp = dp[row+1][col] - dungeon[row][col]
#                     if (hp >= 1):
#                         fromrow = hp
#                     else:
#                         fromrow = 1
#                     fromcol = 0
#                     hp = dp[row][col+1] - dungeon[row][col]
#                     if (hp >= 1):
#                         fromcol = hp
#                     else:
#                         fromcol = 1
#                     print('fromrow: ', fromrow, ', fromcol: ', fromcol)
#                     dp[row][col] = min(fromrow, fromcol)
#                 elif (row == maxrow and col == maxcol):
#                     print('row col: ', row, col)
#                     hp = minhp - dungeon[row][col] 
#                     if (hp >= 1):
#                         dp[row][col] = hp
#                     else:
#                         dp[row][col] = 1
            
#         print('dp: ', dp)
#         return dp[0][0]        
