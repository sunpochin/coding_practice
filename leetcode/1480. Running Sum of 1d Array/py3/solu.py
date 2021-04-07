# Time complexity: O(n)O(n)O(n) where nnn is the length of the input array. This is because we use a single loop that iterates over the entire array to calculate the running sum.
# Space complexity: O(1)O(1)O(1)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for ix in range(1, len(nums) ):
            nums[ix] = nums[ix] + nums[ix - 1]
            # print('ix: ', ix, ', nums[ix]: ', nums[ix])
        return nums
        
        # ret = []
        # prevsum = 0
        # for ix in nums:
        #     prevsum += ix
        #     ret.append(prevsum)
        # return ret

    



