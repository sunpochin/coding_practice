# https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        # dp = [0 for x in range(len(s) + 1)]
        dp = [0] * (len(s)+1)
        # base case init
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for it in range(2, len(s) + 1):
            # 2 steps jump
            if 10 <= int(s[it-2:it]) <= 26: #(3)
                # print('before, dp: ', dp)
                dp[it] += dp[it - 2]
                # print('it-2, dp[', it ,']: ', dp[it])
                # print('after, dp: ', dp)
            # one step jump
            if 0 < int(s[it-1:it]) <= 9:
                # print('before, dp: ', dp)
                dp[it] += dp[it-1]
                # print('it-1, dp[', it ,']: ', dp[it])
                # print('after, dp: ', dp)
        return dp[len(s)]
