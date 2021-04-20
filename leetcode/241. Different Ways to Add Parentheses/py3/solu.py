# expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# left of '2', two brackets most,

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# left of '2', three brackets most.
# (2*(3-(4)*5))


# https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/520018/Easy-understand-DandC-solution-no-helper-function-needed-Pattern-example
# JefferyZZY
# The most difficult part is finding the pattern
# I will set example to show the pattern I found:
# Let's say 2-1-1+1, you can think it like a tree, every time when you read the operator you will split it into left part and right part:

# iteration 1:
# 			2 - 1- 1 + 1
# 		   /   \
# 		  2 - (1-1+1)
# 		 /	   /  \
# 		2	- (1 - (1+1))
		
# 		then
		
# 			2 - 1- 1 + 1
# 		   /   \
# 		  2 - (1-1+1)
# 		 /	     /  \
# 		2 - ((1 -1)+1)
		
# This give us
# 1.  2-(1 - (1+1))=3
# 2.  2 -(1 -1)+1))=1


# iteration 2:
# 		2 - 1 - 1 + 1
# 		    /   \
# 		(2 -1)-(1 + 1)
# this give us
# 1. (2-1)-(1+1) = -1

# iteration 3:
# 			2 - 1- 1 + 1
# 				   /   \
# 		   (2 - 1 - 1) + 1
# 			 / \          \
# 		   (2 - (1 -  1)) +  1
		   
# 		   then 
		   
# 		   2 - 1- 1 + 1
# 				   /   \
# 		   (2 - 1 - 1) + 1
# 			     / \      \
# 		 ((2 - 1) -  1) +  1
# this give us
# 1. 2 - (1 -  1)) +  1=3
# 2. ((2 - 1) -  1) +  1=1

# So the solution is [3,1,-1,3,1]




class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        