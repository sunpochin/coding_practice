# # brute force
# class Solution:
#     dirs = {(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1) }
#     def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
#         print('r: ', r, ', c: ', c)
#         if (r < 0 or c < 0 or r >= N or c >= N):
#             return 0
        
#         if (0 == K):
#             return 1
        
#         res = 0
#         for dir in self.dirs:
#             res += self.knightProbability(N, K - 1, r + dir[0], c + dir[1]) / 8
#             print('res: ', res )
#         print('break:')
#         return res

    
# Memoizing top down DP solution.
class Solution:
    dirs = {(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1) }
    def recurse(self, N: int, K: int, r: int, c: int, dp: []):
        if (r < 0 or c < 0 or r >= N or c >= N):
            return 0
        if (0 == K):
            return 1
#        print('dp[K][r][c]: ', dp[K][r][c])
        if (0 != dp[K][r][c]):
            return dp[K][r][c]
        
        res = 0
#        print('self.dirs: ', self.dirs )
        
        for dir in self.dirs:
            res += self.recurse(N, K - 1, r + dir[0], c + dir[1], dp) / 8
#            print('res: ', res )
#        print('break:')
        dp[K][r][c] = res
        return dp[K][r][c] 
        
        
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K + 1)]
#        dp = [[[0 for x in range(c)] for y in range(r)]]
#        print('K: ', K, ', r: ', r, ', c: ', c, ', dp: ', dp)
        
        return self.recurse(N, K, r, c, dp)

