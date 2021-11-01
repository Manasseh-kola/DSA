"""
Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array.
If the input array is empty, the function should return 0 .

Sample Input
array = [75, 105, 120, 75, 90, 135]
Sample Output
330 // 75 + 120 + 135

"""

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
      return 0
    if len(array)==1:
      return array[0]
    maxSubset = array[:]
    maxSubset[1] = max(array[1],array[0])

    for i in range(2,len(array)):
      maxSubset[i] = max(maxSubset[i-1],maxSubset[i-2] + maxSubset[i])

    return maxSubset[-1]
