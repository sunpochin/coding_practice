# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 and 8 become a fleet, meeting each other at 12.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6.
# Note that no other cars meet these fleets before the destination, so the answer is 3.


# cars:  [(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)]
# times:  [12.0, 3.0, 7.0, 1.0, 1.0]
# lead:  1.0 , times:  [12.0, 3.0, 7.0, 1.0]
# lead:  1.0 , times:  [12.0, 3.0, 7.0]
# lead:  7.0 , times:  [12.0, 3.0]
# lead:  3.0 , times:  [12.0]
# ans:  2 , bool(times):  True , ret:  3



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        # print('cars: ', cars)
        # print('times: ', times)
        ans = 0
        while len(times) > 1:
            # print(', times: ', times)
            lead = times.pop()
            # print('lead: ', lead)
            if lead < times[-1]:
                # if lead arrives sooner, it can't be caught
                # print('lead sooner!: ', lead)
                ans += 1
            else:
                # fleet arrives at later time.
                # print('fleet arrives later: ', lead)
                times[-1] = lead
        
        ret = ans + bool(times)
        # print('ans: ', ans, ', bool(times): ', bool(times), ', ret: ', ret)
        return ret
            
#         for ix in range(5):
#             zipped = zip(position, speed)
#             position = [x + y for (x, y) in zipped]
            
#             print('sum: ', position)
            
                
                
                
