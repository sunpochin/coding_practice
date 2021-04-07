class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = len(nums) // 3
        hmap = {}
        for ix in nums:
            cnt = hmap.get(ix, 0)
            hmap[ix] = cnt + 1
            
        ret = []
        for iy in hmap:
            if hmap[iy] > times:
                ret.append(iy)
        return ret
        