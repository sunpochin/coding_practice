class Solution:
    # https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/discuss/355470/Python%3A-Two-Ways-O(N)-and-O(logN)
    # time complexity: O(log(N) )
    # space comp: O(N) worst case when every element nums is different.
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def search(arr, tar):
            lo, hi = 0, len(arr)
            while(lo < hi):
                mid = (lo + hi) // 2
                print('mid: ', mid)
                if arr[mid] < tar:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        N = len(nums)
        if nums[N // 2] != target:
            return False
        lo = search(nums, target)
        print('lo: ', lo)
        hi = search(nums, target + 1)
        print('lo: ', lo, ', hi: ', hi)
        return hi - lo > N // 2
    
    # time complexity: O(N)
    # space comp: O(N) worst case when every element nums is different.
    # def isMajorityElement(self, nums: List[int], target: int) -> bool:
    #     hmap = {}
    #     for ix in nums:
    #         cnt = hmap.get(ix, 0)
    #         hmap[ix] = cnt + 1
            
    #     if hmap.get(target, 0) > len(nums) / 2:
    #         return True
    #     else:
    #         return False
            

