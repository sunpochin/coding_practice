class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length of the input array
        length = len(nums)
        # left and right arrays as described in the algorithm
        L, R, ans = [0] * length, [0] * length, [0] * length
        # L[i] contains the product of all elements to the left
        # For the element at index '0' there are no elements to the left, 
        # so L[0] would be 1
        L[0] = 1
        for it in range(1, length):
            # L[it] already contains the product of elements to the left of 'it - 1'
            L[it] = nums[it - 1] * L[it - 1]

        # R[it]

        R[length - 1] = 1
        for it in reversed(range(length - 1)):
            # R[it + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[it + 1] would give the product of all
            # elements to the right of index 'it'
            R[it] = nums[it + 1] * R[it + 1]

        # constructing the answer
        for it in range(length):
            ans[it] = L[it] * R[it]
        return ans
    
        
        