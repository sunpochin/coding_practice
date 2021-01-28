class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n + 1)
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for ni in range(3, n + 1):
            print('ni: ', ni)
            dp[ni] = dp[ni - 1] + dp[ni - 2]
            
        return dp[n]
    
    
#     def climb_stairs(self, i: int, n: int) -> int:
#         if (i > n):
#             print('return 0, i: ', i, ', n: ', n)
#             return 0
        
#         if (i == n):
#             print('i: ', i, ', n: ', n, ', return 1')
#             return 1
        
#         print('i + 1: ', i + 1, ', i + 2: ', i + 2)
#         return self.climb_stairs(i + 1, n) + self.climb_stairs(i+2, n)
    
#     def climbStairs(self, n: int) -> int:
#         return self.climb_stairs(0, n)
    
    