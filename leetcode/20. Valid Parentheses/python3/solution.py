#0328
class Solution:
    def isValid(self, s: str) -> bool:
        thestack = []
        leftbra = ['[', '{', '(']
#        themap = {']': '[', '}': '{', ')': '(' }
        themap = {'[': ']', '{': '}', '(': ')' }
        for it in s:
            if it in leftbra:
#                thestack.insert(it, 0)
                thestack.append(it)
#                print('stack: ', thestack)
            else:
                if 0 == len(thestack):
                    return False
                tail = thestack.pop()
#                print('tail: ', tail)
                expecting = themap[tail]
#                print('expecting: ', expecting)
                if expecting == it:
                    continue
                else:
                    return False
        if 0 == len(thestack):
            return True
        else: 
            return False

                


# class Solution:
#     def isValid(self, s: str) -> bool:
#         """
#         :type s: str
#         :rtype: bool
#         """
#         # The stack to keep track of opening brackets.
#         stack = []

#         # Hash map for keeping track of mappings. This keeps the code very clean.
#         # Also makes adding more types of parenthesis easier
        
#         mapping = {")": "(", "}": "{", "]": "["}
        
#         for char in s:
#             if char in mapping:
#                 # ternary condition in python
#                 # https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
#                 top_element = stack.pop() if stack else '#'
#                 # The mapping for the opening bracket in our hash and the top
#                 # element of the stack don't match, return False
#                 if mapping[char] != top_element:
#                     return False
#             else:
#                 # We have an opening bracket, simply push it onto the stack.
#                 stack.append(char)
#         # In the end, if the stack is empty, then we have a valid expression.
#         # The stack won't be empty for cases like ((()
#         return not stack
                
