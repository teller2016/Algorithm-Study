# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/

# 파이썬 방식
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))

# 풀이1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]
        return result

# My
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        cur = prices[0]
        for price in prices:
            if price > cur:
                result += price-cur
            cur = price
        return result