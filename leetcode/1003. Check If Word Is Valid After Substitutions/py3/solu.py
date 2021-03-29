class Solution:
    def isValid(self, s: str) -> bool:
        # try to locate and remove 'abc' from s 
        # if there is no more 'abc' to remove, check if remaining string == ""
        # if ==, it's a valid string, return true.
        # if not, return false.
        
        # constraints: if at the same time exist more than one 'abc' in the string?
        # test case: aabcbcabc, return true.
        
        while(True):
            pos = s.find('abc')
#            print('s: ', s, ', pos: ', pos)
            if pos >= 0:
                s = s.replace('abc', '')
            else:
                if 0 == len(s):
                    return True
                else:
                    return False
