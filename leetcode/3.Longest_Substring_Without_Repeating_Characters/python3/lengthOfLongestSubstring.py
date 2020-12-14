class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng = len(s)
#        print('leng: ', leng)
        hashdict = {}
        i = 0
        j = 0
        ans = 0
        while ((i < leng) and (j < leng) ):
#            print('s[', j, ']: ', s[j])
            if (s[j] not in hashdict):
                hashdict[s[j]] = 1
                j=j+1
                ans = max(ans, j - i)
#                print('ans: ', ans)
            else:
                hashdict.pop(s[i], None)
                i=i+1
        
        return ans
        