class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS = []
        stackT = []
        # print('stackS: ', stackS)
        # print('stackT: ', stackT)

        for s in S:
#            print('s: ', s)
            if '#' == s:
                if len(stackS) > 0:
                    stackS.pop()
            else:
                stackS.append(s)
#            print('stackS: ', stackS)
#        print('stackS: ', stackS)
        
        for t in T:
#            print('t: ', t)
            if '#' == t:
                if len(stackT) > 0:
                    stackT.pop()
            else:
                stackT.append(t)
#            print('stackT: ', stackT)
#        print('stackT: ', stackT)
        return self.CompareStr(stackS, stackT)
    
    def CompareStr(self, stackS: list, stackT: list) -> bool:
        if len(stackS) != len(stackT):
            return False
        for it in range(len(stackS)):
#            print('stackS[it]: ', stackS[it])
            if stackS[it] != stackT[it]:
                return False
        # else
        return True     
