"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
    
        if len(prices) == 0:
            return 0
        profits = [[0 for _ in prices] for _ in range(k+1)]

        for r in range(1,k+1):
            maxBuy = float("-inf")
            for c in range(1,len(prices)):
                maxBuy = max(maxBuy,profits[r-1][c-1]-prices[c-1])
                profits[r][c] = max(profits[r][c-1],maxBuy+prices[c])

        return profits[-1][-1]
