class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP solution.
        aux = [[1 for x in range(n)] for x in range(m)]
        print('aux: ', aux)
        
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1] + aux[i-1][j]
                print('aux: ', aux)
                
        return aux[-1][-1]
        
        # formula solution
        fact = math.factorial(m+n-2) / ( math.factorial(m-1) * math.factorial(n-1) )
        return int(fact)
    