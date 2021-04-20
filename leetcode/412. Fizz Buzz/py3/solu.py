class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for ix in range(1, n + 1):
            tmp = ''
            if ix % 3 == 0:
                tmp += 'Fizz'
            if ix % 5 == 0:
                tmp += 'Buzz'
            if not tmp:
                tmp += str(ix)
            ret.append(tmp)
            # if ix % 15 == 0:
            #     ret.append('FizzBuzz')
            # elif ix % 5 == 0:
            #     ret.append('Buzz')
            # elif ix % 3 == 0:
            #     ret.append('Fizz')
            # else:
            #     ret.append(str(ix))
        return ret
                
        