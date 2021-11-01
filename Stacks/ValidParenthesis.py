"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closingBrackets = {")":"(","}":"{","]":"["}
        
        for bracket in s:
            if bracket not in closingBrackets:
                stack.append(bracket)
            else:
                if len(stack):
                    if closingBrackets[bracket] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                
        return len(stack) == 0
            
        
