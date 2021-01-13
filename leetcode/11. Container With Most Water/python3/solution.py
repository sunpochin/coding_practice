from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        curMaxArea = 0
        idxl = 0
        idxr = len(height) - 1
        while(idxl < idxr):
            curArea = min(height[idxr], height[idxl]) * (idxr - idxl)
            curMaxArea = max(curMaxArea, curArea) 
            if (height[idxl] < height[idxr]):
                idxl = idxl + 1
            else:
                idxr = idxr - 1
        
        return curMaxArea

#         for idx1 in range(len(height)):
# #            print('idx1: ', idx1, 'height[idx1,:]: ', height[idx1:])
# #            print('idx1: ', idx1)
#             for idx2 in range(idx1, len(height) ):
# #                print('idx2: ', idx2)
#                 curArea = (idx2 - idx1) * min(height[idx2], height[idx1])
# #                print('curArea: ', curArea)
#                 if curArea > curMaxArea:
#                     curMaxArea = curArea
        
#         return curMaxArea
                
                