class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minCnt = 0
        freshcnt = 0
        thequeue = []
        # sequential traversal
        for it in range(len(grid) ):
            for iy in range(len(grid[0]) ):
                if (2 == grid[it][iy]):
                    thequeue.append((it, iy) )
                    
                if (1 == iy):
                    freshcnt += 1
        print('freshcnt: ', freshcnt)
        print('thequeue: ', thequeue)
        
        # BFS traversal
        # - Use queue size to track: Minutes.
        # - Process rotten oranges
        # -- rot adjancent fresh oranges
        # -- push into queue
        # -- decrement fresh oranges count

