"""
LeetCode
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        
        maxReach = nums[0]
        steps = nums[0]
        
        
        for i in range(1,len(nums)-1):
            maxReach = max(maxReach,nums[i]+i)
            steps -=1
            if steps == 0:
                if maxReach <= i:
                    return False
                steps = maxReach -i
             
        return True if maxReach >=len(nums)-1 else False
            
