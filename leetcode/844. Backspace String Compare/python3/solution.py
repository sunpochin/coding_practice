class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ptrS, ptrT = len(S) - 1, len(T) - 1
        while(ptrS >= 0 or ptrT >= 0):
            if ('#' == S[ptrS] or '#' == T[ptrT]):
                if '#' == T[ptrT]:
                    backT = 2
                    while(backT > 0):
                        print('ptrT: ', ptrT, ', backT: ', backT)
                        ptrT -= 1
                        backT -= 1
                        if '#' == T[ptrT]:
                            backT += 2
                            
                if '#' == S[ptrS]:
                    backs = 2
                    while(backs > 0):
                        ptrS -= 1
                        backs -= 1
                        print('ptrS: ', ptrS, ', backs: ', backs)
                        if '#' == S[ptrS]:
                            backs += 2
            else:
                # both char are NOT '#', don't need to process, both --
                print('S[ptrS]: ', S[ptrS], ', T[ptrT]: ', T[ptrT])
                if S[ptrS] != T[ptrT]:
                    return False
                else:
                    ptrS -= 1
                    ptrT -= 1
        
        # passed all char comparison without returning False, return True
        return True