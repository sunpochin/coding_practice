# There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# 1. Clarify: what do we mean by: "In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards."
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# so at step 2, which do we take? how many cards?

# Input: cardPoints = [9,2,3,4,5,6,9], k = 3
# case of "head equals to tail"?
# Input: cardPoints = [9,2,3,4,5,100,9], k = 3
# and this case?

# algo: 
# 1. take max(head_node, tail_node)
# 2. pop the taken node. sum up it to sum
# 3. repeat k times.
# 4. return sum.
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
