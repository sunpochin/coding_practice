class Solution:
    
    directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if (0 == len(grid) ):
            return 0
        islandCnt = 0
        for row in range( len(grid) ) :
            for col in range( len(grid[0]) ) :
#                print('row: ', row, ', col: ', col, ', value: ', grid[row][col])
                if '1' == grid[row][col]:
                    print('island found! ', row, col)
                    islandCnt += 1
                    grid[row][col] = 0
                    
                    queue = []
                    queue.append([row, col])
                    
                    while (len(queue)):
                        curPos = queue.pop(0)
                        curRow = curPos[0]
                        curCol = curPos[1]
                        for curDir in self.directions:
                            nextRow = curRow + curDir[0]
                            nextCol = curCol + curDir[1]
                            if (nextRow < 0 or nextRow >= len(grid) or nextCol < 0 or nextCol >= len(grid[0]) ):
                                continue
                            if ('1' == grid[nextRow][nextCol]):
                                queue.append([nextRow, nextCol])
                                grid[nextRow][nextCol] = 0
                            
        
        return islandCnt
    