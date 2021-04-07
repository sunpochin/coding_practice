

# Time Complexity: O(1)
#     There are two operations in the algorithm. First, we do the XOR operation which takes a constant time.
#     Then, we call the built-in bitCount function. In the worst scenario, the function would take O(k)\mathcal{O}(k)O(k) time where kkk is the number of bits for an integer number. Since the Integer type is of fixed size in both Python and Java, the overall time complexity of the algorithm becomes constant, regardless the input numbers.
# Space Complexity: O(1), a temporary memory of constant size is consumed, to hold the result of XOR operation.
#     We assume that the built-in function also takes a constant space. 

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xored = x ^ y
        # print('bin(x ^ y): ', bin(x ^ y))
        res = bin(xored).count('1')
        # print(res)
        return res

