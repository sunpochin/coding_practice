class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        print("matrix: ", matrix)
        n = len(matrix[0])
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                # matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                # print('matrix[j][i]: ', matrix[j][i])
                temp1 = matrix[i][j]
                temp2 = matrix[j][i]  
                matrix[j][i] = temp1
                matrix[i][j] = temp2
        print("matrix: ", matrix)
        # reverse each row
        for i in range(n):
            matrix[i].reverse()        
        
