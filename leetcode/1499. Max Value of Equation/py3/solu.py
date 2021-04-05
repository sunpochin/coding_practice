# lee215
# Explanation

# Because xi < xj,
# yi + yj + |xi - xj| = (yi - xi) + (yj + xj)
# So for each pair of (xj, yj),
# we have xj + yj, and we only need to find out the maximum yi - xi.
# To find out the maximum element in a sliding window,
# we can use priority queue or stack.
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        q = []
        res = -float('inf')
        for x, y in points:
            # we only need points[i] s.t. such that |x_i - x_j| <= k,
            # and because points is already sorted by x,
            # so x_i must <= x_j, the inequality can be expressed as
            # x_j - x_i <= k.
            # we will discard points[i] s.t. x_j - x_i > k
            
            while q and q[0][1] < x - k:
                # print('q to pop: ', q)
                heapq.heappop(q)
            # in which y_j + x_j is solely determined
            # by current point(it serves as points[j]),
            # so what we want to find is the points[i]
            # s.t. i < j and with max (y_i - x_i)                
            if q:
                # print('q left: ', q)
                res = max(res, -q[0][0] + y + x)
                # print('res: ', res)
            #  Since Python provides min-heap, we would stuff (xj - yj, xj) to the queue 
            # such that top of the queue has points with largest y-x and x could 
            # be used to verify if the constraint is met.
            heapq.heappush(q, (x-y, x))
            # print('x: ', x, ', y:', y, ', heap push q: ', q)
        return res


