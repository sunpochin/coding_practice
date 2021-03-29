# 2, 1, 0
# 1, 1, 0
# 0, 1, 1

# after 1 min
# 2, 2, 0
# 2, 1, 0
# 0, 1, 1

# after 2 min
# 2, 2, 0
# 2, 2, 0
# 0, 1, 1

class Solution:
    
    directions = [[-1, 0], 
                [0, 1],
                [1, 0],
                [0, -1]]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if 0 == len(grid):
            return 0
        
        ROTTEN = 2
        FRESH = 1
        EMPTY = 0
        
        freshcnt = 0
        rot = []
        # sequential traversal
        for row in range(len(grid) ):
            for col in range(len(grid[0]) ):
                if (ROTTEN == grid[row][col]):
                    rot.append([row, col])
                    
                if (FRESH == grid[row][col]):
                    freshcnt += 1
        print('freshcnt: ', freshcnt)
        print('rot: ', rot)
        
        # BFS traversal
        # - Use queue size to track: Minutes.
        # - Process rotten oranges
        # -- rot adjancent fresh oranges
        # -- push into queue
        # -- decrement fresh oranges count
        
        minCnt = 0
        curQueSize = len(rot)
        while(len(rot) > 0):
#            print('len(rot): ', len(rot))
            # print('len(rot): ', len(rot), ', rot: ', rot)
            if (0 == curQueSize):
                curQueSize = len(rot)
                # one minute passed
                minCnt += 1
                print('minutes passed: ', minCnt)
            curOrange = rot.pop(0)
            print('rot popped: len(rot): ', len(rot), ', rot: ', rot, ', curOrange: ', curOrange)
            curQueSize -= 1
            row = curOrange[0]
            col = curOrange[1]
            
            for curDir in Solution.directions:
                nextrow = row + curDir[0]
                nextcol = col + curDir[1]
                if (nextrow < 0 or nextrow >= len(grid) or nextcol < 0 or nextcol >= len(grid[0])):
                    continue
                if (FRESH == grid[nextrow][nextcol]):
                    grid[nextrow][nextcol] = ROTTEN
                    freshcnt -= 1
                    rot.append([nextrow, nextcol])
#                    print('rot appended: ', len(rot))
                    print('rot appended: len(rot): ', len(rot), ', rot: ', rot)
                    print('grid: ', grid)

        if (freshcnt != 0):
            return -1
        
        return minCnt
            
            
            