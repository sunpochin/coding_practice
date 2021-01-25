class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fact = math.factorial(m+n-2) / ( math.factorial(m-1) * math.factorial(n-1) )
        return int(fact)
    

