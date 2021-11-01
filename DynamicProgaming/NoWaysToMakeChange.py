"""
Given an array of distinct positive integers representing coin denominations and a single
non-negative integer n representing a target amount of money, write a function that
returns the number of ways to make change for that target amount using the given coin
denominations. Note that an unlimited amount of coins is at your disposal

Sample Input
n = 6
denoms = [1, 5]

Sample Output
2 // 1x1 + 1x5 and 6x1
"""


def numberOfWaysToMakeChange(n, denoms):
    numberOfWays = [0 for i in range(n+1)]
    numberOfWays[0] = 1

    for denom in denoms:
      for i in range(1,len(numberOfWays)):
        if denom <= i:
          numberOfWays[i] += numberOfWays[i-denom]

    return numberOfWays[n]
