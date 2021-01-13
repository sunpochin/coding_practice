

class Solution:
    def searchPair(self, nums, target, left, triplets):
        right = len(nums) - 1
        while(left < right):
            curSum = nums[left] + nums[right]
            if (curSum == target):
                triplets.append([-target, nums[left], nums[right]] )
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1  # skip same element to avoid duplicate triplets
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1  # skip same element to avoid duplicate triplets
            elif curSum < target:
                left += 1
            else:
                right -= 1
        
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print('nums: ', nums)
        nums.sort()
        print('nums: ', nums)
        triplets = []
        for it in range(len(nums)):
            # skip same element to avoid duplicate triplets
            if it > 0 and nums[it] == nums[it-1]:  
                continue
#            self.searchPair(it+1)
            self.searchPair(nums, -nums[it], it+1, triplets)    
        return triplets            
        
            
            
            
        