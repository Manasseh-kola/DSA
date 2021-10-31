"""
LeetCode 42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    def trap(self, height: List[int]) -> int:

        x = len(height)-2
        maxR = [x:= i+1 if height[i+1] > height[x] else x for i in reversed(range(len(height)-1))][::-1]
        maxR.append(0)

        fluid = [0 for _ in height]
        start = 0
        maxLeft = 0
        for i in range(len(height)-1):
            fill = min(maxLeft,height[maxR[i]])
            amount = fill - height[i] if height[i] < fill else 0
            fluid[i] = amount
            maxLeft = max(maxLeft,height[i])

        return sum(fluid)
	
