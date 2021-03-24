class Solution:
    # brute force
    dirs = {(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1) }
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        print('r: ', r, ', c: ', c)
        if (r < 0 or c < 0 or r >= N or c >= N):
            return 0
        
        if (0 == K):
            return 1
        
        res = 0
        for dir in self.dirs:
            res += self.knightProbability(N, K - 1, r + dir[0], c + dir[1]) / 8
            print('res: ', res )
        print('break:')
        return res

    
#     def recurse(self, curPos, dir8):
# #        dir8 = {(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1) }
#         if (curPos[0] >=  or curPos[1] >= 0):
#             return False
#         for iy in range(dir8):
#             newPos = (curPos[0] + iy[0], curPos[0] + iy[1])
#             print('newPos:', newPos)
            
            
# #        newPos = (curPos[0] + dir[0], curPos[0] + dir[1])
# #        newPos = curPos + dir
                
#     def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
#         # brute force first.
#         dir8 = {(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1) }
#         curPos = (r, c)
#         for it in range(K):
#             # knight goes from (r, c), to 8 directions.
#             for dir in dir8:
#                 curPos = self.recurse(curPos, dir8)
