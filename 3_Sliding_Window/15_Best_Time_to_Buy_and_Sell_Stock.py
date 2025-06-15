"""
Problem: Best Time to Buy and Sell Stock
Link: https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150
Category: Sliding Window
Created on: 6/14/2025

Approach:
- Use the sliding window technique of variable size to find the max profit between days in the list
- Adjusted l pointer if value of r was less than value of l to find better day to buy
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        profit = 0
        for r in range(len(prices)):
            profit = max(profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        return profit

test = Solution()
print(test.maxProfit([10,8,7,5,2]))