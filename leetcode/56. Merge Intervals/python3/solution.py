class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            print('interval: ', interval)
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or (merged[-1][1] < interval[0]):
                # print('merged[-1][1]: ', merged[-1][1])
                merged.append(interval)
                # print('merged[-1][1]: ', merged[-1][1])
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                # print('else ')
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        
        return merged


