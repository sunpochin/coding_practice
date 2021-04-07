# time comp: O(N)
# space complexity: O(N)
class Solution:
    def removeVowels(self, s: str) -> str:
        ret = ''
        vowelset = {'a', 'e', 'i', 'o', 'u'}
        for ix in s:
            if ix in vowelset:
                pass
            else:
                ret += ix
        return ret
