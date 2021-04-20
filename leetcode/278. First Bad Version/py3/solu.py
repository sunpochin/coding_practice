# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# Binary Search!

# If you are setting mid=left+right/ 2 , you have to be very careful. Unless you are using a language that does not overflow such as Python, left+right could overflow. One way to fix this is to use left + (right−left) / 2 instead.

# Time complexity: O(log n)
# Space : O(1)

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while (left < right):
            mid = int(left + (right - left) / 2)
            isbad = isBadVersion(mid)
            # print('left: ', left, ', right: ', right, ', mid: ', mid, ', isbad: ', isbad)
            if isbad == False:
                left = mid + 1
            else:
                right = mid
        return left
            # if left == right:
            #     # print('equal: ', left, right, mid)
            #     return left
            #     # return mid
        