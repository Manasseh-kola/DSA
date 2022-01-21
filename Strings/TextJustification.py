"""
Leetcode 68. Text Justification
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        allLines = []
        letters = 0
        for w in words:
            if len(w)+len(line)+letters > maxWidth:
                for i in range(maxWidth-letters):
                    line[i%(len(line)-1 or 1)] += " "
                allLines.append("".join(line))
                line = []
                letters = 0
                
            line.append(w)
            letters +=len(w)
            
        allLines.append(" ".join(line).ljust(maxWidth))
        return allLines
            
        
