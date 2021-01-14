from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        ans = collections.defaultdict(list)
        for s in strs:
            print('s: ', s)
            print('sorted s: ', sorted(s) )
            print('tuple(sorted(s)): ', tuple(sorted(s) ) )
#            ans[sorted(s) ].append(s)
            ans[tuple(sorted(s) )].append(s)
        print('ans.values: ', ans.values(), ', ans: ', ans)
        return ans.values()
