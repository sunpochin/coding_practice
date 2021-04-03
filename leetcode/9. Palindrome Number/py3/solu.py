class Solution:
    def palinstr(self, strx: str):
        print('strx: ', strx)
        if len(strx) == 1:
            return True
        if len(strx) == 0:
            return True
        front = strx[0]
        back = strx[len(strx) - 1]
        remains = strx[1:len(strx) - 1]
        return back == front and self.palinstr(remains)

    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) / 10
            ranger /= 100

        return True    
    
    
    # def isPalindrome(self, x):
    #     if x > 0:
    #         temp = x
    #         rev_int_elements = []
    #         while temp > 0:
    #             digit = temp % 10
    #             rev_int_elements.append(digit)
    #             print('rev_int_elements: ', rev_int_elements)
    #             temp = temp // 10
    #         org_int_elements = rev_int_elements[::-1]
    #         return rev_int_elements == org_int_elements
    #     elif x == 0:
    #         return True
    #     else:
    #         return False
#     def isPalindrome(self, x: int) -> bool:
#         print('abs: ', str(abs(x))[::-1] )        
#         return int(str(abs(x))[::-1]) == x

#     def isPalindrome(self, x: int) -> bool:
#         strx = str(x)
#         ret = self.palinstr(strx)
#         print('\n')
#         return ret
    
        
        
