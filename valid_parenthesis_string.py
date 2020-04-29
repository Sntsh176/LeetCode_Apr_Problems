"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""



class Solution:
    def checkValidString(self, s: str) -> bool:
    
        stack_left = []
        stack_star = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack_left.append(i)
            elif s[i] == '*':
                stack_star.append(i)
            else:
                if len(stack_left) == 0 and len(stack_star) == 0:
                    return False
                if len(stack_left):
                    stack_left.pop()
                else:
                    stack_star.pop()
        
        while stack_left and stack_star:
            if stack_left[-1] > stack_star[-1]:
                return False
            else:
                stack_left.pop()
                stack_star.pop()
        
        return len(stack_left) == 0