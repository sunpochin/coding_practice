from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print('matrix.shape[0]: ', len(matrix) )
        rCnt = len(matrix)
        cCnt = len(matrix[0])
        print('m: ', rCnt, ', n: ', cCnt)
        rows, cols = set(), set()
        
        # mark the rows and columns that are to be made zero
        for ni in range(rCnt):
            for nj in range(cCnt):
                if matrix[ni][nj] == 0:
                    rows.add(ni)
                    cols.add(nj)
        # go over the array again, using the rows and cols sets to update the elements
        for ni in range(rCnt):
            for nj in range(cCnt):
                if ni in rows or nj in cols:
                    matrix[ni][nj] = 0
                    
            
