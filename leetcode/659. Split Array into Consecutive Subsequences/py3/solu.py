# used a greedy algorithm.
# leftis a hashmap, left[i] counts the number of i that I haven't placed yet.
# endis a hashmap, end[i] counts the number of consecutive subsequences that ends at number i    

# https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/C%2B%2BPython-Esay-Understand-Solution
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/311938/Just-visual-description-(had-a-lot-of-English-trouble-from-solution-descriptions)

class Solution:
    def isPossible(self, A):
        left = collections.Counter(A)
        end = collections.Counter()
        for i in A:
            if not left[i]: 
                print('not exist: ', i, left[i])
                continue
            left[i] -= 1
            print('i: ', i, ', left[i] -= 1: ', left[i])
            # adding to a existing subsequence length >= 3 ends at i-1
            if end[i - 1] > 0:
                print('end: ', end)
                end[i - 1] -= 1
                end[i] += 1
                print('after end: ', end)
            # "existing subsequence length >= 3 ends at i-1" doesn't exist, start a new subsequence of 3, 
            # by left[i+1] -= 1 
            # left[i+2] -= 1
            # end[i + 2] += 1
            elif left[i + 1] and left[i + 2]:
                print('left: ', left)
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
                print('after left: ', left, ', end: ', end)
            else:
                print('False: left: ', left, ', end: ', end, '\n')
                return False
        print('\n')
        return True
        