# "aaaaaaa"
# ["aaaa","aaa"]
# "goalspecial"
# ["go","goal","goals","special"]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hmap = {}
        for ix in wordDict:
            hmap[ix] = hmap.get(ix, 0) + 1
        print(hmap)
        
        lp, rp = 0, 0
        for rp in range(len(s)):
            cur = s[lp:rp + 1]
            print('s[lp:rp + 1]: ', cur)
            if hmap.get(cur, 0) >= 1:
                print('found!', cur)
                lp = rp+1
                # end case
                left = s[lp:len(s)]
                print('left:', left)
                if hmap.get(left, 0) >= 1:
                    return True
                
            print('lp: ', lp, ', rp: ', rp, 'cur:', cur)
        if lp == rp + 1:
            return True
        else:
            return False        