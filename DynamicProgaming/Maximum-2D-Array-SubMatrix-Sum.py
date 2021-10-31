"""
Given a two-dimensional array of potentially unequal height and width filled with integers and a positive integer size . Write a
function that returns the maximum sum that can be generated from a submatrix with dimensions size * size .
For example, consider the following matrix:
[
 [2, 4],
 [5, 6],
 [-3, 2],
]
If size = 2 , then the 2x2 submatrices to
consider are:
[
[2, 4]
[5, 6]
]

[
[5, 6]
[-3, 2]
]

The sum of the elements in the first submatrix is 17, and the sum of the elements in the second submatrix is 10. In this example, your function should return 17.
"""

def maximumSumSubmatrix(matrix, size):
    sums = prefixSum(matrix)
    maxSum = float("-inf")

    for r in range(len(sums)):
      L = 0; R = size
      T = r; B = r + size
      if B>= len(sums):
        break
      while R < len(sums[0]):
        currSum = sums[B][R] - sums[B][L] - sums[T][R] + sums[T][L]
        maxSum = max(currSum,maxSum)
        L+=1;R+=1

    return maxSum
			
def prefixSum(matrix):
    sums = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
    sums[1][1] = matrix[0][0]

    for c in range(1,len(matrix[0])):
      sums[1][c+1] = sums[1][c] + matrix[0][c]

    for r in range(1,len(matrix)):
      sums[r+1][1] = sums[r][1] + matrix[r][0]

    for r in range(2,len(sums)):
      for c in range(2,len(sums[0])):
        sums[r][c] = sums[r-1][c] + sums[r][c-1] - sums[r-1][c-1] + matrix[r-1][c-1]

    return sums
