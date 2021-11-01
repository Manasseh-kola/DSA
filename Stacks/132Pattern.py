"""
456. 132 Pattern

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)< 3:
            return False
        
        nextGreater = {}
        stackG = []
        lowest = float("inf")
        
        for num in nums:
            while len(stackG) and num >= stackG[-1]:
                stackG.pop()
                
            if len(stackG):
                if stackG[-1] in nextGreater :
                    if (num not in nextGreater[stackG[-1]]):
                        nextGreater[stackG[-1]].add(num)
                else:
                    nextGreater[stackG[-1]] = {num}
            stackG.append(num)
         
        for num in nums:
            if num not in nextGreater:
               
                lowest =min(lowest,num)
            else: 
                currentGreater = nextGreater[num]
                lowest = min(num,lowest)
                for two in currentGreater:
                    if lowest < two:
                        return True

        return False
