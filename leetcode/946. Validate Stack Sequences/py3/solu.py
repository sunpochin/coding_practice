# https://leetcode.com/problems/validate-stack-sequences/discuss/197685/C%2B%2BJavaPython-Simulation-O(1)-Space
# Solution1: Simulating

# Initialize am empty stack,
# iterate and push elements from pushed one by one.
# Each time, we'll try to pop the elements from as many as possibile popped.
# In the end, we we'll check if stack is empty.

# Time O(N)
# Space O(N)

# Solution 2: Using pushed as Stack
# Based on the solution 1,
# @aravind-kumar suggested using pushed as the stack.
# This solution will take O(1) extra space,
# though it also changed the input.
# Time O(N)
# Space O(1) 
# be more precise during interview: O(1) extra space, O(N) modified space

# Solution 2:
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for ix in pushed:
            stack.append(ix)
            print('ix: ', ix)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                print('stack[-1]: ', stack[-1], ', popped[j]: ', popped[j])
                stack.pop()
                j+=1
        
        return j == len(popped)
