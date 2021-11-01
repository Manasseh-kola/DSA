"""
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac"."

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stackS = []
        stackT = []
        i =0
        while i < len(s):
            if s[i] == "#" :
                if len(stackS):
                    stackS.pop()
            else:
                stackS.append(s[i])
            i +=1
            
        i = 0
        while i < len(t):
            if t[i] == "#":
                if len(stackT):
                    stackT.pop()
            else:
                stackT.append(t[i])
            i +=1
            
        return ("".join(stackS))==("".join(stackT))
        
    
 
            
