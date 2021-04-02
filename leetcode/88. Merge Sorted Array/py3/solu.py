class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy for the first m elements
        nums1_copy = nums1[:m]
        # read pointers for p1 and p2
        p1, p2 = 0, 0
        # Compare elements from nums1copy and nums2 and write smallest to nums1
        for p in range(n + m):
            # we also need to ensure that p1 and p2 aren't over boundaries
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
        