"""
Write a function that takes in an array of integers and returns the largest possible value for the expression
array[a] - array[b] + array[c] - array, where a , b , c , and d are indices of the array and a < b < c < d .
If the input array has fewer than 4 elements, your function should return 0 .
Sample Input
array = [3, 6, 1, -3, 2, 7]
Sample Output
4
"""

def maximizeExpression(array):
    if len(array) < 4:
      return 0
    minVal = -abs(min(array)*len(array)*2)
    maxSums = [[minVal for _ in array] for _ in range(4) ]

    prev = minVal
    for c in range(len(array)-3):
      maxVal = max(array[c],prev)
      maxSums[0][c] = maxVal
      prev = maxVal

    for r in range(1,4):
      for c in range(r,len(array)-(4-(r+1))):
        curr = array[c] if r%2 ==0 else -array[c]
        maxVal = max(maxSums[r-1][c-1]+curr,maxSums[r][c-1])
        maxSums[r][c] = maxVal

    return maxSums[-1][-1]
