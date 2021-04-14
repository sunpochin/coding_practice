class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = ['']
        self.inp = []
        def recur(res, idx):
            if idx == len(self.inp):
                return
            print(self.inp, idx)
            cur = self.inp[idx]
            tmp = []
            for i in res:
                for j in cur:
                    ij = i + j
                    print('ij:', ij, ', i:', i, ', j:', j)
                    tmp.append(ij)
            print('tmp:', tmp)
            recur(tmp, idx + 1)
                
                
        inp = []
        for i in digits:
            if '2' is i:
                self.inp.append('abc')
            if '3' is i:
                self.inp.append('def')
        print(self.inp)
        recur(res, 0)
        
        return res        
            
            
                