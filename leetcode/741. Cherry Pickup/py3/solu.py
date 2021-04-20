# Input: grid = [
# [ 1, 1,-1],
# [ 1,-1, 1],
# [-1, 1, 1]]
# Output: 0

#  grid = [
# [0,1,-1],
# [1,0,-1],
# [1,1,1]]
# Output: 5

# [0,      1==1+0,             -1],
# [1==1+0, 2==1+1,             -1],
# [2==1+1(self), 3==2+1(self), 4==3(left)+ 1(self) ]]

# [0, 1, -1],
# [0, 0, -1],
# [0, 0, 0]]
# ===
# [0, 1, -1],
# [1, 2, -1],
# [2, 3,  4]]
# ===

# [0, 0, 0],
# [0, 0, 0],
# [0, 0, 0]]
# ===
# [0, 0, 0],
# [0, 0, 0],
# [0, 0, 0]]



# [0, 0, 0],
# [0, 0, 0],
# [0, 0, 0]]
# ===
# [0, 0, 0],
# [0, 0, 0],
# [0, 0, 0]]




# algorithm:
# * Cherry/1 after being picked up, should be set to 0, for calculating returning route.

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        