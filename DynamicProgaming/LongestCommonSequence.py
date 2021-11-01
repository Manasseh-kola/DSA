"""
Write a function that takes in two strings and returns their longest common subsequence.
A subsequence of a string is a set of characters that aren't necessarily adjacent in the string but that are in the same order as they appear in the string. For instance, the
characters ["a", "c", "d"] form a subsequence of the string "abcd" , and so do the characters ["b", "d"] . Note that a single character in a string and the string itself
are both valid subsequences of the string. You can assume that there will only be one longest common subsequence.

Sample Input
str1 = "ZXVVYZW"
str2 = "XKYKZPW"
Sample Output
["X", "Y", "Z", "W"]
"""

from collections import deque
def longestCommonSubsequence(str1, str2):
    matches = [[0 for i in range(len(str1)+1)] for i in range(len(str2)+1)]
    for r in range(1,len(str2)+1):
      for c in range(1,len(str1)+1):
        if str1[c-1] == str2[r-1]:
          matches[r][c] = matches[r-1][c-1]+1
        else:
          matches[r][c] = max(matches[r][c-1],matches[r-1][c])

    return backTrack(matches,str1,str2)

def backTrack(matches,str1,str2):
    r = len(str2)
    c = len(str1)
    longest = deque([])

    while r > 0 and c>0:
      if matches[r][c] == matches[r][c-1]:
        c-=1
      elif matches[r][c] == matches[r-1][c]:
        r-=1			
      else:
        longest.appendleft(str1[c-1])
        r-=1
        c-=1

    return list(longest)
