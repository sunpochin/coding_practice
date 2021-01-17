class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
        # MAXIMUM SUBARRAY - CODING INTERVIEW QUESTION
        # https://www.youtube.com/watch?v=5WZl3MMT0Eg 
        for it in range(1, len(nums) ):
            if nums[it - 1] > 0:
                nums[it] = nums[it] + nums[it - 1]
                
        return max(nums)
        