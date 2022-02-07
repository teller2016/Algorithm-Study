#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        result = 0
        for price in prices:
            min_price = min(min_price, price)
            result = max(result, price-min_price)
        return result