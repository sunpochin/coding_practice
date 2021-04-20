class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ret = set()
        def dfs(curval, sum, depth):
            if depth == n:
                ret.add(sum)
                return
            sum = sum * 10 + curval 
            if curval + k <= 9:
                dfs(curval + k, sum, depth + 1)
            if curval - k >= 0:
                dfs(curval - k, sum, depth + 1)
        for it in range(1, 10):
            dfs(it, 0, 0)
        # print('ret: ', ret)
        return ret