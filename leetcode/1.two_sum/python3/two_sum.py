from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        for x in nums:
            for y in nums:
                if target == (x + y):
                    ret=[x, y]
        return ret

    def test_twoSum(self):
        nums = [2,7,11,15]
        target = 9
        sol = Solution() 
        result = sol.twoSum(nums, target)
        print('result: ', result)

        

