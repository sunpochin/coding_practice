

class Solution:
    def searchPair(self, nums, target, left, triplets):
        right = len(nums) - 1
        while(left < right):
            curSum = nums[left] + nums[right]
            if (curSum == target):
                triplets.append([nums[left], nums[right], -target] )
                left += 1
                right -= 1
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
#            self.searchPair(it+1)
            self.searchPair(nums, -nums[it], it+1, triplets)    
        return triplets            
        
            
            
            
        