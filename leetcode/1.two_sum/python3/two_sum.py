from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        
        hashdict = {}
        
        for itx, x in enumerate(nums, start=0):
            hashdict[x] = itx
            
        print('hashdict: ', hashdict)
        for itx, x in enumerate(nums, start=0):
            compen = target - x
            if (compen in hashdict) and (itx != hashdict[compen]):
                print('compen: ', compen)
                ret = [itx, hashdict[compen]]
                return ret
            
#        return ret

#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ret = []
#         for itx, x in enumerate(nums, start=0):
#             for ity, y in enumerate(nums[itx + 1:], start=itx+1):
# #                print("nums[itx + 1:]: ", nums[itx + 1:])
# #                print("itx:", itx)
#                 if target == (x + y):
#                     ret=[itx, ity]
#         return ret
