# Intuition / Algorithm
# Set a direction to do Deep first search, 
# if 'blocked': 'hit wall' / 'hit already visited element', then 'turn right'.
# 'turn right' means, if going to right, change dir to down. If going down, change to left. If going left, change to up. Going up, change to right.
# If all of 4 ways are blocked, end DFS.

# 1 2 3 1 2 
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1 

# x x x x x 
# x x-> 1 x
# x 1 1 1 x
# x x x x x 

# x x x x x 
# x x-> 1 x
# x 1 1 1 x
# x 1 1 1 x
# x x x x x 

# [[1,2,3,4],
#  [4,5,68,1],
#  [7,8,9,12]]

################################
# AN INTERVIEW FRIENDLY SOLUTION
################################
# https://leetcode.com/problems/spiral-matrix/discuss/20599/Super-Simple-and-Easy-to-Understand-Solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if None == matrix or 0 == len(matrix):
            return res
        n = len(matrix)
        m = len(matrix[0])
        up, down, left, right = 0, n - 1, 0, m - 1
        print('n*m: ', n*m)
        while(True):
            print('1. res: ', res)
            for ix in range(left, right + 1):
                print('ix: ', ix, ', matrix[up][ix]: ', matrix[up][ix])
                res.append(matrix[up][ix])

            if (len(res) >= n*m):
                break
            print('2. ix: ', ix, len(res), 'up + 1: ', up + 1, ', down - 1: ', down -1)
            for iy in range(up + 1, down):
                print('iy: ', iy, ', matrix[iy][right]: ', matrix[iy][right])
                res.append(matrix[iy][right])
            if (len(res) >= n*m):
                break

            print('3. right left: ', right, left)
            for ix in range(right, left - 1, -1):
                print('ix: ', ix, ', matrix[down][ix]: ', matrix[down][ix])
                res.append(matrix[down][ix])
            if (len(res) >= n*m):
                break
                
            print('4. down-1 up+1: ', down-1, up+1)
            for iy in range(down - 1, up, -1):
                print('iy: ', iy, ', matrix[iy][left]: ', matrix[iy][left])
                res.append(matrix[iy][left])
            if (len(res) >= n*m):
                break
                
            print('end of 4 for loops, res: ', res, len(res))
            left += 1
            right -= 1
            up += 1
            down -= 1
        return res
