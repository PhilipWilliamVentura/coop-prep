# Pattern: Sliding Window
# Time: O(n) | Space: O(1)
# Tripped up on: Straight forward problem
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            if prices[r] <= prices[l]:
                l = r
            r += 1
        return profit