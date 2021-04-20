class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        sum = [0] * (len(nums) + 1)
        sum[0] = 0
        for ix in range(1, len(nums) + 1 ):
            sum[ix] = sum[ix - 1] + nums[ix - 1]
            # print('sum[', ix, ']: ', sum[ix])
        for start in range(len(nums) + 1):
            for end in range(start + 1, len(nums) + 1):
                if sum[end] - sum[start] == k:
                    cnt += 1
        return cnt
        
        # brute force
        # anscnt = 0
        # for ix in range(len(nums) ):
        #     sum = 0
        #     for iy in range(ix, len(nums) ):
        #         sum += nums[iy]
        #         # print('nums[iy]:', nums[iy], ', sum: ', sum)
        #         if k == sum:
        #             anscnt += 1
        #             # print('anscnt: ', anscnt)
        # return anscnt
        