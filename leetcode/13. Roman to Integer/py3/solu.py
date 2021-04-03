# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# Thoughts:
# char list: ['I', 'V', 'X', 'L', 'C', 'D', 'M']
# cases:
# 4   I,V 0,1
# 9   I,X 0,2

# 40  X,L 2,3
# 90  X,C 2,4

# 400 C,D 4,5
# 900 C,M 4,6

# 5   V   1
# 50  L   3
# 500 D   5

# CC is 200, CCC is 300, XC is 90, CD 400, CM 900
# L is 50, XL is 40,
# X is 10, XX is 20, IX is 9

# detect each char of s
# If detect 'I', next is more 'I' or 'V', or 'X', or other?
# If detect 'X', next is more X, or 'L', or 'C', or other?
# If detect 'C', next is more C, or 'D', or 'M', or other?
# If detect 'M', next is more M?

class Solution:
    def romanToInt(self, s: str) -> int:
        reversed = s[::-1]
        # print('rev: ', reversed)
        hmap = {}
        stack = []
        sum = 0
        # charlist = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        charlist = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        for it in reversed:
            if 'I' == it:
                if hmap.get('V'):
                    sum -= 1
                elif hmap.get('X'):
                    sum -= 1
                else:
                    hmap[it] = 1
                    sum += 1

            if 'X' == it:
                if hmap.get('L'):
                    sum -= 10
                    # hmap['D'] is 0
                elif hmap.get('C'):
                    sum -= 10
                    # hmap['M'] is 0
                else:
                    hmap[it] = 1
                    sum += 10
            
            if 'C' == it:
                # if D or M show, -100, else + 100
                # print('D: ', hmap.get('D'))
                if hmap.get('D'):
                    sum -= 100
                    hmap['D'] is 0
                elif hmap.get('M'):
                    sum -= 100
                    hmap['M'] is 0
                else:
                    hmap[it] = 1
                    sum += 100
                    
            if 'M' == it:
                hmap[it] = 1
                sum += 1000

            if 'D' == it:
                hmap[it] = 1
                sum += 500
                # print('hmap: ', hmap)

            # if 'C' == it:
            #     hmap[it] = 1
            #     sum += 100
            if 'L' == it:
                hmap[it] = 1
                sum += 50

            # if 'X' == it:
            #     hmap[it] = 1
            #     sum += 10
            if 'V' == it:
                hmap[it] = 1
                sum += 5
                
                
        return sum
                
                
                
        

